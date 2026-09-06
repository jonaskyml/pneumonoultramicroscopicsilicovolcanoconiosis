from pathlib import Path
import click




@click.command()
@click.argument('filename')
# @click.option("--file", prompt='File name', help='Scan file for the longest word.')

def scan(filename: str):
    """Scan dictionary for the longest word."""

    with open(filename, 'r', encoding="utf-8") as file:
        i = 0
        word_longest = ""

        for line in file:
            if not line.strip():
                continue

            length_current = len(line.strip())

            if length_current > i:
                word_longest = line.strip()
                length_longest = length_current
                i = length_current

        if not word_longest.strip():
            click.echo("The file is empty!")
        else:
            #  click.echo(f"word: '{word_longest}' | legnth: '{length_longest}'")
            click.echo(word_longest)
            click.echo(length_longest)