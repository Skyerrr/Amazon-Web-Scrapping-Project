from src.infra.html_filter import IphoneHtmlFilter

"""
Scrap from Amazon
Str: change SEARCH_PARAMETER with your selected product to be scrapped and return a csv file
"""

if __name__ == "__main__":

    SEARCH_PARAMETER = "iphone"

    scrapper = IphoneHtmlFilter()

    scrapper.run_from_url(
        f"https://www.amazon.com.br/s?k={SEARCH_PARAMETER}", f"{SEARCH_PARAMETER}.csv"
    )
    # scrapper.run_from_html_file("response2.html", CSV_FILE_NAME)
