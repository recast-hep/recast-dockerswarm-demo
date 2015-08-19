import shutil
import os
import yaml
from adage import adagetask

from fileaccess import rsrc
from subprocessctx import subprocess_in_env

import logging 
log = logging.getLogger(__name__)

@adagetask
def first_task(workdir,argument):
  log.info("executing first task with argument {}".format(argument))
  with subprocess_in_env() as check_call:
    # check_call('echo {} {}'.format(argument,workdir))
    check_call('echo {} > {}/first.txt'.format(argument,workdir))
      
      
@adagetask
def second_task(workdir,argument,suffix):
  log.info("executing second task with argument {}".format(argument))
  with subprocess_in_env() as check_call:
    check_call('echo {} > {}/second-{}.txt'.format(argument,workdir,suffix))
        
@adagetask
def third_task(workdir,argument):
  log.info("executing third task with argument {}".format(argument))
  with subprocess_in_env() as check_call:
    check_call('echo {} > {}/third.txt'.format(argument,workdir))
