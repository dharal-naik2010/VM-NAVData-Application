#To calculate CAGR for each mutual fund.

def calculate_each_fund_cagr(group):

    group = group.sort_values("Date")

    beginning_nav = group.iloc[0]["NAV"]
    ending_nav = group.iloc[-1]["NAV"]

    beginning_date = group.iloc[0]["Date"]
    ending_date = group.iloc[-1]["Date"]
    
    years = (ending_date - beginning_date).days / 365.25

    cagr = (ending_nav / beginning_nav) ** (1 / years) - 1

    return cagr * 100 #cagr in percentage


#To calculate CAGR for all the mutual funds

def calculate_all_funds_cagr(df):

    results = []

    for fund_name, group in df.groupby("Mutual Fund"):
        cagr = calculate_each_fund_cagr(group)

        results.append({"Mutual Fund":fund_name, "CAGR": cagr})
        
    return results
