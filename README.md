# `zip-code-area`

## Description

Get a map of zip codes and their surrounding zip codes that are within a given radius.

## Installation

With [Git](https://git-scm.com/downloads), [Python](https://www.python.org/downloads/), and [Poetry](https://python-poetry.org/docs/) installed, simply run the following command to get the project on your machine.

```bash
git clone https://github.com/dawsonbooth/zip-code-area
```

## Usage

The following is an example usage of the project:

```bash
python src/main.py zips.txt --radius 5 > out.txt
```

The `out.txt` file then contains:

```txt
75001
75002
75006
75007
75010
75013
75023
75024
75025
75034
75035
75039
75042
75056
75059
75066
75068
75074
75075
75080
75081
75093
75205
75206
75209
75220
75225
75229
75230
75231
75234
75235
75238
75240
75243
75244
75248
75251
75252
75254
75287
75806
76025
```

Additionally, with this program, you can generate a URL to a map of the zip code boundaries!

Here's an example:

```bash
python src/main.py zips.txt --radius 5 --map --title "Close Proximity Area"
```

...which outputs this URL: https://www.randymajors.com/p/customgmap.html?zips=75035,75240,75074,75225,75001,75252,75034,75080,75068,75081,75287,75042,75230,75010,75056,75231,75025,75205,75229,75251,75066,75059,75024,76025,75039,75209,75235,75806,75007,75013,75254,75248,75006,75243,75075,75093,75220,75002,75206,75023,75234,75244,75238&title=Close+Proximity+Area

## License

This software is released under the terms of [MIT license](LICENSE).
