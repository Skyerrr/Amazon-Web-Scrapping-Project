import csv
from request_url import UrlToScrap
import pandas as pd
from bs4 import BeautifulSoup


class IphoneHtmlFilter(UrlToScrap):
    """
    Filter Html file OR Request to CSV
    """

    def __init__(self) -> None:
        self.price_list = []
        self.names = []

    def parse_iphone(self, html: str, csv_file_name="results.csv") -> None:
        """
        Filter Iphone name and price from request or file
        """

        soup = BeautifulSoup(html, "lxml")
        containers = soup.find_all("div", class_="s-card-container")
        print(len(containers))
        # self.names = [
        #     container.find_all("span", "a-size-base-plus a-color-base a-text-normal")[
        #         0
        #     ].text
        #     for container in containers
        # ]
        for container in containers:
            try:
                name = container.find_all(
                    "span", "a-size-base-plus a-color-base a-text-normal"
                )[0].text
                self.names.append(name)
            except (IndexError, AttributeError):
                try:
                    name = container.find_all(
                        "span", "a-size-base a-color-base a-text-normal"
                    )[0].text
                    self.names.append(name)
                except (IndexError, AttributeError):
                    name = "N/A"
                    self.names.append(name)

        for container in containers:
            try:
                price_whole = container.find_all("span", "a-price-whole")[0].text
                price_fraction = container.find_all("span", "a-price-fraction")[0].text
                price = price_whole + price_fraction

                self.price_list.append(price)
            except (IndexError, AttributeError):
                price = None
                self.price_list.append(price)

        self.data_to_csv(csv_file_name)

    def data_to_csv(self, csv_file_name="results.csv") -> csv:
        """
        Transform data from request or file to CSV
        """
        results = []

        for index in range(0, len(self.names)):
            results.append({"name": self.names[index], "price": self.price_list[index]})

        to_csv = pd.DataFrame(results)
        to_csv.to_csv(csv_file_name, index=False)

    def run_from_url(self, url: str, csv_file_name="results.csv") -> csv:
        """
        Run direct from URL
        """

        response = self.fetch(url)
        self.parse_iphone(response[1], csv_file_name)

    def run_from_html_file(self, html_file: str, csv_file_name="results.csv") -> csv:
        """
        Run direct from HTML file, must be in same directory
        """

        html = ""
        with open(html_file, "r", encoding="utf-8") as html_file:
            for line in html_file.read():
                html += line
        self.parse_iphone(html, csv_file_name)
