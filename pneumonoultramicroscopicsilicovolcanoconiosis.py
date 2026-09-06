import click
import crud

@click.group()
@click.version_option(
    version="0.1.0",
    prog_name="pneumonoultramicroscopicsilicovolcanoconiosis",
    message="%(prog)s %(version)s"
)

def cli() -> None:
    pass

cli.add_command(crud.scan)