# lab2

2. Create 2a.py
i. After used command python . i saw:
We are in the __main__
2020-11-07 19:41:26.848578
win32

3. Result pytho. -h:
usage: . [-h] [-o OPT] [-l]

Приклад передачі аргументів у Python програму.

optional arguments:
  -h, --help            show this help message and exit
  -o OPT, --optional OPT
                        Цей параметр є вибірковим.
  -l, --logs            Якщо виконати команду з цим параметром будуть
                       виводитись логи.
4. Command python3 . -o "This text ..." gave the result:
We are in the __main__
2020-11-07 20:16:33.526964
linux
З консолі було передано аргумент
 This text ...
5. python3 . --logs message:
2020-11-07 20:19:56,231 root INFO: Тут буде просто інформативне повідомлення
2020-11-07 20:19:56,231 root WARNING: Це Warning повідомлення
2020-11-07 20:19:56,231 root ERROR: Це повідомлення про помилку
 