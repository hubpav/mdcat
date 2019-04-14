'Markdown-friendly variant of cat'

import click
import grp
import os
import pwd

__version__ = '1.0.0'


@click.command(context_settings={"ignore_unknown_options": True})
@click.argument('files', nargs=-1, type=click.Path(exists=True))
@click.version_option(version=__version__)
def main(files):
    try:
        first = True
        for file in files:
            path = os.path.abspath(file)
            stat = os.stat(path)
            if first:
                first = False
            else:
                click.echo()
            click.echo('File: `{}` (`{} {}:{}`):'.format(
                path,
                oct(stat.st_mode)[4:],
                pwd.getpwuid(stat.st_uid).pw_name,
                grp.getgrgid(stat.st_gid).gr_name)
            )
            click.echo()
            with open(path, 'r') as f:
                for count, line in enumerate(f):
                    click.echo('    {}'.format(line.rstrip()))
    except KeyboardInterrupt:
        pass
