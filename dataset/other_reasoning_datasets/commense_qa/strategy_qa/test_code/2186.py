def solution():
    authentic_knighthood_countries = ["United Kingdom"]
    medieval_times_show_knights = True
    if "United States" not in authentic_knighthood_countries and medieval_times_show_knights:
        result = "not authentic"
    else:
        result = "authentic"
    return result

print(solution())