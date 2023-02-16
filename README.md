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