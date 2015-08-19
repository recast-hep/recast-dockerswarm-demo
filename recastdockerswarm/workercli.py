import subprocess
import click

@click.command()
def cli():
  cmd = ['celery','worker','-A','recastdockerswarm.fromenvapp:app','-I','recastdockerswarm.adagetasks','-l','info','-c','1']
  p = subprocess.Popen(cmd)
  p.communicate()
  

  