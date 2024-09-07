import pandas as pd
from datetime import datetime as dt 

<<<<<<< HEAD
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
=======
now = dt.now()
print(now)
print("Test")
>>>>>>> c8b8335fafab189ed6a4edab9b1e6dc71396e6a2
