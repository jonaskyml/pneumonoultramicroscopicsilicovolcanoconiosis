from pathlib import Path
import click




@click.command()
@click.argument('filename')
# @click.option("--file", prompt='File name', help='Scan file for the longest word.')

def scan(filename: str):
    """Scan dictionary for the longest word."""

    with open(filename, 'r', encoding="utf-8") as file:
        content = file.read().splitlines()

    for word in content:
        if not word.strip():
            continue

        length = len(word)

        click.echo(f"word: '{word}' | legnth: '{length}'")
