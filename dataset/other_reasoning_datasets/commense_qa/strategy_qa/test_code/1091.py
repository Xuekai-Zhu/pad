def solution():
    # Define the countries that the Sea of Japan touches
    sea_of_japan_countries = ["Japan", "Russia", "Korea"]
    # Check if Japan is the only country that the Sea of Japan touches
    if len(sea_of_japan_countries) == 1 and sea_of_japan_countries[0] == "Japan":
        result = "yes"
    else:
        result = "no"
    return result

print(solution())