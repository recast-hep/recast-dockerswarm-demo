import os
import logging
import yaml
import click
import adage
from adage import mknode

from fileaccess import rsrc,workdir_access_methods
from adagetasks import *

def build_dag(workdir):
  inwrk,inpt = workdir_access_methods(workdir)
  dag,rules = adage.mk_dag(), []

  mknode(dag,first_task.s(workdir,'hello'))
  a = mknode(dag,second_task.s(workdir,'what?','a'))
  b = mknode(dag,second_task.s(workdir,'yeah!','b'))
  mknode(dag,third_task.s(workdir,'done soon!'), depends_on = [a,b])

  return dag,rules


from fromenvapp import app as celery_app

@click.command()
@click.argument('workdir')
@click.option('-l','--logger',default = __name__)
def cli(workdir,logger):
  logging.basicConfig(level = logging.INFO)

  log = logging.getLogger(logger)
  dag,rules = build_dag(workdir)
  log.info('running dilepton from workdir {0}'.format(workdir))
  try:
    adage.rundag(dag,rules,backendsubmit = adage.celerysetup(celery_app))
  except RuntimeError:
    log.error('DAG execution failed')
    raise click.Abort
  
  log.info('done')
