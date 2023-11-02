def solution():
    num_gallons = 3
    ounces_per_gallon = 128
    drank_ounces = 13

    # Calculate the total number of ounces of milk James originally had
    total_ounces = num_gallons * ounces_per_gallon

    # Calculate the number of ounces of milk James has left
    remaining_ounces = total_ounces - drank_ounces
    result = remaining_ounces
    return result

print(solution())