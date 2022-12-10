# Copyright © 2022 mightyK1ngRichard <dimapermyakov55@gmail.com>
import threading
import time

RES = False
def foo1():
    count = 0
    while True:
        count += 1
        time.sleep(1)
        if count % 2 == 0:
            global RES
            RES = True
            print('stop')
            return


def main():
    t1 = threading.Thread(target=foo1, args=())
    t1.start()
    while True:
        if RES:
            break
        print('>>>')
        time.sleep(1)
    print('end')
if __name__ == '__main__':
    main()