## Install the required software
1/ Programming language: Python 3.9 or latest\
2/ IDE: PyCharm (Community Edition) or Visual studio code\
3/ Source control: Git\
4/ Browsers: Chrome, Firefox, Edge Chromium


## Install dependencies
```
$ pip install -r requirements.txt
```

## Switching between browser
Go to file "./common/config.json", change value of "ui_browser": "{name_browser}"\
With replacing "{name_browser}":\
1/ "chrome" - for Chrome browser or\
2/ "firefox" - for Firefox browser or\
3/ "edge' - for Edge Chromium browser


## Execute the test
```
$ pytest -v features/test_search_city.py --html=report/test_search_city_report.html --self-contained-html
```

- `-v` option to show test result on console
- more test option please refer to `https://docs.pytest.org`

# Viewing Test report
```report\{report_name}.html```