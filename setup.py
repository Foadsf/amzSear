from setuptools import setup, find_packages
setup(
  name = 'amzsear',
  packages = find_packages(),
  version = '2.0.1',
  description = 'The unofficial Amazon search CLI & Python API',
  author = "Asher Silvers",
  author_email = "ashersilvers@gmail.com",
  license='MIT',
  url = 'https://github.com/asherAgs/amzSear', 
  keywords = 'amazon search product products python',
  classifiers = [],
  entry_points={
    'console_scripts': [
      'amzsear = amzsear.cli.cli:run',
     ],
  },
  install_requires=[
    "lxml>=4.9.1",
    "cssselect>=1.1.0",
    "lxml_html_clean>=0.1.0",
    "requests>=2.20.0",
  ],
)
