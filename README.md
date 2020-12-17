## Install the required software
1/ Programming language: Python 3.9 or latest\
2/ IDE: PyCharm (Community Edition) or Visual studio code\
3/ Source control: Git


## Install dependencies
```
$ pip install -r requirements.txt
```

## Execute the test
```
$ pytest -v features/test_search_city.py --html=report/test_search_city_report.html --self-contained-html
```

- `-v` option to show test result on console
- more test option please refer to `https://docs.pytest.org`

# Viewing Test report
```report\{report_name}.html```