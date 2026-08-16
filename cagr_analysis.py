#To find top mutual funds with highest CAGR.

def find_top_performers(cagr_results, number_of_mfs):

    sorted_results = sorted(cagr_results, key = lambda x: x["CAGR"], reverse = True)

    return sorted_results[:number_of_mfs]
    

#To find mutual funds with lowest CAGR.

def find_low_performers(cagr_results, number_of_mfs):

    sorted_results = sorted(cagr_results, key = lambda x: x["CAGR"], reverse = False)

    return sorted_results[:number_of_mfs]