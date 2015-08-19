from setuptools import setup, find_packages

setup(
  name = 'recast-dockerswarm-demo',
  version = '0.0.1',
  description = 'recast-dockerswarm-demo',
  url = '',
  author = 'Lukas Heinrich',
  author_email = 'lukas.heinrich@cern.ch',
  packages = find_packages(),
  include_package_data = True,
  install_requires = [
    'adage',
    'click',
    'pyyaml',
    'celery',
    'redis'
  ],
  entry_points = {
      'console_scripts': ['recastworkflow-headnode=recastdockerswarm.headcli:cli',
                          'recastworkflow-workernode=recastdockerswarm.workercli:cli']
  },
  dependency_links = [
  ]
)
