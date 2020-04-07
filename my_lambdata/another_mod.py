# my_lambdata/class2.py

import pandas

def convert_names(my_df):
    """
    Create a new column called "state_name" which has the corresponding
    state name.

    Params my_df(pandas.DataFrame) with column called "abbrev" which has state
    abbrevs
    """
    # GIVEN: dataframe with column called "abbrev" which has state abbrevs
    # GOAL: create a new column called "state_name" which has the corresponding
    #. state name
    df = my_df.copy()
    names_map = {
        "AL": "Alabama",
        "CT": "Conn",
        "CA": "Cali",
        "CO": "Colo",
        "DC": "District of Columbia"
    }
    print(type(df["abbrev"])) #> <class 'pandas.core.series.Series'>
    df["state_name"] = df["abbrev"].map(names_map)
    return df


if __name__ == "__main__":
    
    df = pandas.DataFrame({"abbrev": ["CT", "CO", "CA", "TX"]})
    full_df = convert_names(df)
    print(full_df.head())

    df2 = pandas.DataFrame({"abbrev": ["GA", "NY", "CA", "CO"]})
    full_df2 = convert_names(df2)
    print(full_df.head())