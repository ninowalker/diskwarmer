from setuptools import setup

setup(name='diskwarmer',
      version='0.1.5',
      description='tool to help warm disk caches by targeting files which were memory resident in vmtouch reports',
      url='http://github.com/livefyre/diskwarmer', #TODO FIX
      author='andrew thomson',
      author_email='andrew@livefyre.com',
      license='MIT',
      packages=['diskwarmer'],
      install_requires = ['pyparsing', 'docopt'],
      entry_points = {
        'console_scripts': [
          'diskwarmer = diskwarmer:main',
          ],
      },
      zip_safe=False)
