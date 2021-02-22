# LEL Express Tracker (DEPRECATED)

***This package has been deprecated. https://tracker.lel.asia/ is no
longer available so the program will not work anymore.***

Track the status of your LEL Express (Lazada eLogistics) packages.

## Usage

You can provide your tracking number as an argument to track_package.py:

    # replace <package_id> with your package number
    python track_package.py <package_id>

If an argument is not provided you will be asked to input your tracking number
when track_package.py in runned.

### Track File
If you dont want to enter your package number everytime, you can create a 'lel.track' file
and place it in the same directory as track_package.py.

## Requirements

1. BeautifulSoup

    pip install beautifulsoup4
