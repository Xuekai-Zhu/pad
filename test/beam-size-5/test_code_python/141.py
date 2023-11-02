def solution():
    
    # Define the number of hectares and pineapples per hectare
    hectares = 10
    pineapples_per_hectare = 100

    # Calculate the total number of pineapples harvested in a year
    total_pineapples = hectares * pineapples_per_hectare * 12

    # Calculate the number of pineapples harvested in a year
    harvested_pineapples_per_year = total_pineapples * 3

    # return the result
    result = harvested_pineapples_per_year
    return result

print(solution())