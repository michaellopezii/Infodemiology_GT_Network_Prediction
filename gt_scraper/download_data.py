"""
This code was originally created to the team of Chu et al. 
for their open sourced-work.

Chu, A. M. Y., Chong, A. C. Y., Lai, N. H. T., Tiwari, A., & So, M. K. P. (2023). 
Enhancing the Predictive Power of Google Trends Data Through Network Analysis: 
Infodemiology Study of COVID-19. 
JMIR Public Health and Surveillance, 9. https://doi.org/10.2196/42446
"""

from pytrends.request import TrendReq

from os import remove, mkdir
from os.path import exists, join
import time

"""
Singleton Initiation
"""
pytrend = TrendReq(
    hl='en-US', tz=0,
    backoff_factor=5
)  # Start request session

def download_data(directory, tag, region, range_start, range_end, days, proxies):

    if proxies == []:
        global pytrend
    else:
        pytrend = TrendReq(
            hl='en-US', tz=0,
            backoff_factor=0.5,
            proxy=proxies
        )

    filename = join(directory, range_start.strftime("%Y %m %d"))

    if not exists(directory):
        mkdir(directory) 

    if exists(filename):
        print(f"[w] {filename} already exist. Skipping...")
        return
    else:
        print(f"[w] Downloading {filename}...")
        pytrend.build_payload(kw_list=[tag],
                            cat=0,
                            timeframe=f"{range_start} {range_end}",
                            geo=region,)
        df = pytrend.interest_over_time()

        if(len(df) < days):
            print(f"[w] [{filename}] is incompleted. Saving as partial")
            filename += ".partial"
        else:
            partial_filename = f"{filename}.partial.csv"
            
            if exists(partial_filename):
                remove(partial_filename)
        
        filename += ".csv"
        df.to_csv(filename)