import sys
sys.path.append('..')

from TestWhl import HelloWorld

def mainFunc():
    print('From other tester:')
    HelloWorld.sayHello()

if __name__ == '__main__':
    mainFunc()
