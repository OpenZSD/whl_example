from setuptools import setup
import setuptools

setup(name = 'TestWhl',
      version = '1.0.0',
      author = 'Test',
      author_email = 'Tester@fakeDomain.com',
      description = 'An example of a whl file',
      url = 'www.fakeurl.com',
      package_dir = { 'TestWhl': 'TestWhl',
                      'OtherTestWhl': 'OtherTestWhl' },
      packages = setuptools.find_packages(),
      package_data = {
        'TestWhl':['content/hello.txt']
      },
      install_requires=['Flask==1.1.2',
                        'Flask-RESTful==0.3.8'],
      entry_points = {
        'console_scripts': ['testwhl = TestWhl.test:sayHello',
                            'othertestwhl = OtherTestWhl.otherTest:mainFunc']
      })

