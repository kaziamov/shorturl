from string import ascii_letters, digits
from random import choices

DEFAULT_LENGTH = 5
DEFAULT_SYMBOLS = ascii_letters + digits + '_!-'
UNIQUE_SYM_COUNT = len(DEFAULT_SYMBOLS) ** DEFAULT_LENGTH


def main():
    print(generate_path())


def generate_link(custom=False):
    if custom:
        return custom
    return generate_path()


def generate_path():
    return choices(DEFAULT_SYMBOLS, k=DEFAULT_LENGTH)


if __name__ == "__main__":
    main()
    # print(f"Unique {UNIQUE_SYM_COUNT}")
