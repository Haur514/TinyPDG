import csv
import glob
import re

project="math"
project_num=106

aggregatedata = list()

# ある階層以下にある,project_idから始まるcsvファイルをすべて取得する
def get_csv_file_with_projectId(project_id):
    return glob.glob("/home/h-yosiok/Lab/KusumotoLab/Lab/TinyPDG/out/"+project_id+"*.csv")

        
def _aggregate_csv(files,project_id):
    for file in files:
        f = open(file,"r")
        datalist = csv.reader(f)
        for data in datalist:
            if(len(data)==0):
                continue
            if(data[0]=="node"):
                continue
            line=re.split('[-.]',str(file))[-2]
            print(line)
            data_in=int(data[1])
            data_out=int(data[2])
            controll_in=int(data[3])
            controll_out=int(data[4])
            aggregatedata.append([project_id,line,data_in,data_out,controll_in,controll_out])
    
            

def write_aggregate_data_as_csv():
    f=open("./../data/edge_info.csv","w")
    for c in aggregatedata:
        f.write(c[0])
        f.write(",")
        f.write(str(c[1]))
        f.write(",")
        f.write(str(c[2]))
        f.write(",")
        f.write(str(c[3]))
        f.write(",")
        f.write(str(c[4]))
        f.write(",")
        f.write(str(c[5]))
        f.write("\n")
    f.close()

print(get_csv_file_with_projectId("math001")[0])
_aggregate_csv(get_csv_file_with_projectId("math001"),"math001")

for i in range(1,project_num):
    _project_id=project+str(i).zfill(3)
    _aggregate_csv(get_csv_file_with_projectId(_project_id),_project_id)

write_aggregate_data_as_csv()