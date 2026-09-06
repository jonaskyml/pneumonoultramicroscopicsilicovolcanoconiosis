from pathlib import Path
import click




@click.command()
@click.argument('filename')
# @click.option("--file", prompt='File name', help='Scan file for the longest word.')



def scan(filename: str):
    """Scan dictionary for the longest word."""

    dictionaries = ["en", "cz"]

    if Path(filename).exists(): # + is it contained in dictionares array
        sourcefile = click.prompt(
            f"\nWhich of the following do you wish to scan?\n\n    [0] Built-in dictionary ({filename})\n    [1] Local file ({filename})\n",
            type=click.Choice(["0", "1"]),
            show_choices=False
        )

    if sourcefile == "1":
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
                click.echo(f"\n{word_longest}")
                click.echo(length_longest)
    else:
        click.echo("you chose a dictionary")
        # code for accessing the dictionary

