# pdf-project

PDFファイルを冊子印刷するためのプログラム。
出力されたファイルを「両面印刷・片面に２枚」で印刷すると冊子になる。  
両面印刷は「短辺とじ」に設定すること。

## Directions
1. Put original pdf files into `input`.
2. Run `merger.py` in terminal.
3. Sorted files will appear in `output`.
4. Setting should be "両面印刷（短辺綴じ）", "片面2枚をまとめる".

## Files & Directories
- `booklet.py`: Make booklet version of each pdf files in `input`.
- `merger.py`: (old program)
- `input`
- `output`
