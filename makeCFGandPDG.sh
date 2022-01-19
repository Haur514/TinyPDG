#! /bin/bash

set -euxo pipefail

readonly DIR=${1%/}
readonly cfg=${DIR}/cfg
readonly pdg=${DIR}/pdg

./gradlew run --args="-d ${DIR} -c ${cfg}.dot -p ${pdg}.dot"

dot.exe -T png ${cfg}.dot -o ${cfg}.png
dot.exe -T png ${pdg}.dot -o ${pdg}.png
