import pandas as pd
from datetime import datetime as dt 

country = {"India": ["Delhi", "Maharashtra", "Haryana", "Uttar Pradesh", "Himachal Pradesh"], "Japan": ["Hokkaido", "Chubu", "Tohoku", "Shikoku", "0"]}
country_df = pd.DataFrame.from_dict(country)

def main():
    now = dt.now()
    print(now)
    print(country_df)
    # for key, val in country.items():
    #     for i in val:
    #         print(i)
    # for key, val in country.items():
    #     for i in val:
    #         print("{} : {}".format(key, i))



if __name__ == "__main__":
    main()