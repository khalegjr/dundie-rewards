import argparse


def main():

    parser = argparse.ArgumentParser(
        description="Dunder Mifflin Rewards CLI",
        epilog="Enjoy and use with cautious.",
    )
    parser.add_argument(
        "subcomand",
        type=str,
        help="The subcommand to run",
        choices=("load", "show", "send")
    )
    parser.add_argument(
        "filepath",
        type=str,
        help="File path to load",
    )

    args = parser.parse_args()

    print("Executing entry point for dundie...")


if __name__ == "__main__":
    main()
