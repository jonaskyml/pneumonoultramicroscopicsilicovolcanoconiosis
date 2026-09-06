from pathlib import Path
import click




@click.command()
@click.argument('filename')
# @click.option("--file", prompt='File name', help='Scan file for the longest word.')

def scan(filename: str):
    """Scan dictionary for the longest word."""

    with open(filename, 'r', encoding="utf-8") as file:
        content = file.read().splitlines()

    i = 1

    for word in content:
        if not word.strip():
            continue

        length_current = len(word)

        

        if length_current >= i:
            word_longest = word
            length_longest = length_current
            i = length_current


    #  click.echo(f"word: '{word_longest}' | legnth: '{length_longest}'")
    click.echo(word_longest)

