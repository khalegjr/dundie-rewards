import click
import pkg_resources

from dundie import core


@click.group()
@click.version_option(pkg_resources.get_distribution("dundie").version)
def main():
    """Dunder Mifflin Rewards System.

    This cli application controls DM rewards.
    """


@main.command()
@click.argument("filepath", type=click.Path(exists=True))
def load(filepath):
    """Loads the file to the database."""
    result = core.load(filepath)
    header = ["name", "dept", "role", "e-mail"]

    for person in result:
        print("-" * 50)
        for key, value in zip(header, person.split(",")):
            print(f"{key.strip()} -> {value.strip()}")
