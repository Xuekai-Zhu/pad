def solution():
    
    # Define the number of hectares and pineapples per hectare
    hectares = 10
    pineapples_per_hectare = 100

    # Calculate the total number of pineapples
    total_pineapples = hectares * pineapples_per_hectare

    # Calculate the number of pineapples harvested in a year
    pineapples_per_year = total_pineapples * 12

    # Display the number of pineapples harvested in a year
    result = pineapples_per_year
    return result

print(solution())