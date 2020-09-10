# Archdaily

This is a scraper for get project's photos of [Archdaily](https://www.archdaily.com/).

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install [Scrapy](https://scrapy.org/).

```bash
pip install -r requirements.txt
```

## Usage

1. Add project's url to urls.txt (Each project in one line)
2. Run spider:

```shell
scrapy runspider archdaily/spiders/projects_spider.py
```

3. View scraped photos at projects folder.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)
