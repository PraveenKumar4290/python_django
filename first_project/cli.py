import click
import os
from rich.console import Console

console=Console()

@click.group()
def cli():
    pass

@cli.command()
@click.argument('project_name')
@click.option('--force', is_flag=True, help='Skip confirmation')
def run(val):
    nums=[1,2,3,4]
    if val not in nums:
        print('Successfully Done...!')
        return True
    
if __name__=='__main__':
    cli()