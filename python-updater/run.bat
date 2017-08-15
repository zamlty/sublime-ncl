@echo off
python main.py
copy completions-function.txt+completions-resources.txt+completions-keywords.txt+completions-codes.txt+completions-ctables.txt+completions-colors.txt /b completions.txt
pause
