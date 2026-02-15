import sys
from pathlib import Path

from colorama import Fore, Style, init


def print_tree(dir_path: Path, indent: int = 0) -> None:
    prefix = " " * 4 * indent

    print(f"{prefix}{Fore.BLUE}{dir_path.name}/{Style.RESET_ALL}")

    try:
        items = sorted(dir_path.iterdir(), key=lambda p: p.name)
    except PermissionError:
        print(f"{prefix}    {Fore.RED}Permission denied{Style.RESET_ALL}")
        return

    for item in items:
        item_prefix = " " * 4 * (indent + 1)

        if item.is_dir():
            print_tree(item, indent + 1)
        else:
            print(f"{item_prefix}{Fore.GREEN}{item.name}{Style.RESET_ALL}")


def main() -> None:
    init()

    if len(sys.argv) < 2:
        print("Usage: python main.py <path_to_directory>")
        sys.exit(1)

    root = Path(sys.argv[1])

    if not root.exists():
        print(f"Path does not exist: {root}")
        sys.exit(1)

    if not root.is_dir():
        print(f"Path is not a directory: {root}")
        sys.exit(1)

    print_tree(root)


if __name__ == "__main__":
    main()
