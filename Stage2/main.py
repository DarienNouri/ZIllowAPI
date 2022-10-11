import json
import locationPresets
from run_scrape import run
import pandas as pd


def main(url=None, startprice=None):
    if url is not None:
        run(url)
    else:
        filters = locationPresets.makeSelection()

        #print(filters[1]['price_min']['min'] = new_price)
        payload = run(presetFilters=filters[0][1])




if __name__ == "__main__":
    main()
