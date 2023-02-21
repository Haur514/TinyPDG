_get_d4j_param() {
    _key=$1
    cat $d4jProperties |
        grep $_key |
        sed "s/$_key=\(.\+\)/\1/" |
        sed 's/,/\n/g' |
        sed "s/::.\+//" |
        sort |
        uniq |
        sed "s/\./\//g"
}

_get_d4j_faultfiles() {
    # d4jのプロジェクトがあるディレクトリ
    base="/home/h-yosiok/Lab/KusumotoLab/exceptionhunter/"
    for i in $(seq 1 100); do
        project="Defects4J-[math$i]/"
        targetDir=$base$project
        d4jProperties=$targetDir"defects4j.build.properties"
        testsDir=$targetDir$(_get_d4j_param d4j.dir.src.tests)"/"
        for test in $(echo $(_get_d4j_param d4j.tests.trigger)); do
            test=$testsDir$test
            echo $test".java"
        done
    done
}

_get_d4j_faultline(){
    # faultdataの入ったファイルのあるディレクトリ
    base="/home/h-yosiok/Lab/KusumotoLab/Lab/h-yosiok_kGenProg/data/"
    file=$base$1
    cat $file | jq -r '.[].id'
    cat $file | jq -r '.[].lineNumber'
}

# math004 -> mathを抽出する
_format_d4j_id(){
    before=$1
    echo ${before:0:4}
}

echo $(_get_d4j_faultline faultData-math.json)
# ./gradlew run --args="-d ./src/test/java/test001 -p ./out/pdg.dot -c ./out/cfg.dot"
