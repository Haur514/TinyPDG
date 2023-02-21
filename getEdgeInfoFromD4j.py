import json
import re
import subprocess


# _get_relative_path_of_fault_fileの返り値をcsvファイルとして出力する
def write_relative_path_of_fault_file_as_csv(_fault_dict, _output_filename):
    f = open(_output_filename, "w")
    data_list=_get_relative_path_of_fault_file(_fault_dict)
    for data in data_list:
        file=data[0]
        line=data[1]
        f.write(file)
        f.write(",")
        f.write(str(line))
        f.write("\n")
    f.close()


# _get_relative_path_of_fault_fileの返り値を利用し，tinypdgを動かす
def _run_tinypdg(_fault_dict):
    data_list=_get_relative_path_of_fault_file(_fault_dict)
    for data in data_list:
        id=data[0]
        file=data[1]
        line=data[2]
        cmd="./gradlew run --args='-d "+file+" -e out/"+id+"-"+str(line)+".csv -l "+str(line)+"'"
        subprocess.run(cmd,shell=True)

# 読み込んだ欠陥のjsonファイルをdict形式で返す


def _get_fault_data_as_dict(filename):
    base = "/home/h-yosiok/Lab/KusumotoLab/Lab/h-yosiok_kGenProg/data/"
    file = base+filename
    json_open = open(file)
    json_load = json.load(json_open)
    return json_load

# _get_fault_data_as_dictで与えられるdict形式のデータから，欠陥を含むファイルのパスと欠陥を含む行番号を取得し，タプルで返す


def _get_relative_path_of_fault_file(fault_dict):
    ret = list()
    for data in fault_dict:
        data_id = data["id"]
        data_file = data["fileName"]
        data_line = data["lineNumber"]
        ret.append([data_id,_get_d4j_fault_file_path(
            "/home/h-yosiok/Lab/KusumotoLab/exceptionhunter/", data_id, data_file), data_line])
    return ret

# math001 -> math1


def _format_fault_id(fault_id):
    matchobj = re.search('\d', fault_id)
    index = matchobj.start()
    id_str = fault_id[0:index]
    id_int = str(int(fault_id[index:]))
    return id_str+id_int

# d4jプロジェクトの欠陥箇所を含むファイルのパスを返す


def _get_d4j_fault_file_path(_base, _id, _relative_file_path):
    format_id = _format_fault_id(_id)
    target_path = _base+"Defects4J-["+format_id+"]/"
    d4j_prop_file = target_path+"defects4j.build.properties"
    src_path = _get_d4j_src_path(d4j_prop_file)
    return target_path+src_path+"/"+_relative_file_path


# defects4j.build.propertiesを読み込み，ソースコードの入ったディレクトリのパスを返す
# return例: src/main/java
def _get_d4j_src_path(d4j_build_properties_file):
    f = open(d4j_build_properties_file)
    datalist = f.readlines()
    f.close()
    for data in datalist:
        if "d4j.dir.src.classes" in data:
            data_split = data.split("=")
            return data_split[1].replace("\n", "")


# print(_get_d4j_fault_file_path("/home/h-yosiok/Lab/KusumotoLab/exceptionhunter/","math001","hoge"))
fault_dict = _get_fault_data_as_dict("faultData-math.json")

# write_relative_path_of_fault_file_as_csv(fault_dict,"./out/test.csv")
_run_tinypdg(fault_dict)