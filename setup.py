from setuptools import setup

setup(name='diskwarmer',
      version='1.0.0',
      description='Tool to help warm disk caches by targeting files which were memory resident in vmtouch reports.',
      url='http://github.com/andrewguy9/diskwarmer',
      author='Andrew Thomson',
      author_email='athomsonguy@gmail.com',
      license='MIT',
      packages=['diskwarmer'],
      install_requires = ['pyparsing', 'docopt'],
      entry_points = {
        'console_scripts': [
          'diskwarmer = diskwarmer:main',
          ],
      },
      classifiers=[
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3',
        'Topic :: Database',
        'Topic :: System :: Filesystems',
        'Topic :: System :: Systems Administration',
        'Programming Language :: Python :: 3'],
      zip_safe=False)
