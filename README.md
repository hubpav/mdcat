# mdcat - Markdown-friendly variant of cat

Ever struggling quickly documenting your server configuration files in a Git repo or sharing them with your colleagues for the future reference? Welcome to **mdcat**.

It is a simple Python 3 command line utility, ingesting file path(s) arguments, and printing their content in Markdown-friendly format.

Moreover, it prints the file's absolute path, mode (permissions), and owner (user + group).

## Requirements

* Python3 + PIP

## Installation

Install/upgrade the tool from PyPI using:

    $ pip3 install --upgrade mdcat

## Usage

    $ mdcat --help
    Usage: mdcat [OPTIONS] [FILES]...

    Options:
      --version  Show the version and exit.
      --help     Show this message and exit.

Example:

    $ echo foo >> bar
    $ mdcat bar

Output:

    File: `/home/pavel/mdcat/bar` (`0644 pavel:users`):

        foo

## Contributing

Please read [**CONTRIBUTING.md**](https://github.com/hubpav/mdcat/blob/master/CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [**SemVer**](https://semver.org/) for versioning. For the versions available, see the [**tags on this repository**](https://github.com/hubpav/mdcat/tags).

## Authors

* [**Pavel Hübner**](https://github.com/hubpav) - Initial work

## License

This project is licensed under the [**MIT License**](https://opensource.org/licenses/MIT/) - see the [**LICENSE**](https://github.com/hubpav/mdcat/blob/master/LICENSE) file for details.
