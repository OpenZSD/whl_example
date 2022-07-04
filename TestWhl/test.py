import sys
sys.path.append('..')

import os
import TestWhl

from TestWhl import HelloWorld

def sayHello():
    print('From tester:')
    HelloWorld.sayHello()
    print(os.path.dirname(os.path.realpath(TestWhl.__file__)))
    print(TestWhl.__file__)
    rp = os.path.dirname(os.path.realpath(TestWhl.__file__))
    print(os.path.join(rp, 'content/hello.txt'))
    with open(os.path.join(rp, 'content/hello.txt'), 'r') as f:
        print(f.read())

if __name__ == '__main__':
    sayHello()

