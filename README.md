TinyPDG
=======

A library for building intraprocedural PDGs for Java programs

[TinyPDG](https://github.com/YoshikiHigo/TinyPDG)のフォーク

実験に必要なデータを収集する


# How To Use
## Out put pdg and cfg
```sh
./gradlew run --args="-d path/to/srcfile -p ./pdg.dot -c ./cfg.dot"
dot -Tpdf pdg.dot -o pdg.pdf
```

## Out put edge info
追加したオプション

```
./gradlew run --args="-d path/to/srcfile -e path2outputfile"
```
`-d`で指定したファイルのデータ依存グラフを作成し，
各ノードにおける，
1. データ依存エッジの入力数
2. データ依存エッジの出力数
3. コントロール依存エッジの入力数
4. コントロール依存エッジの出力数
を指定したファイルに出力する．
データ形式は`csv`