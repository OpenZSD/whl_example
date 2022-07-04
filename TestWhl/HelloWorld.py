import sys
sys.path.append('..')

import os
import TestWhl

def sayHello():
    print("hello from module")

    rp = os.path.dirname(os.path.realpath(TestWhl.__file__))
    print(os.path.join(rp, 'content/hello.txt'))
    with open(os.path.join(rp, 'content/hello.txt'), 'r') as f:
        print(f.read())
