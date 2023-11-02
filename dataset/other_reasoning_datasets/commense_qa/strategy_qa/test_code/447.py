def solution():
    # Define Betsy Braddock's height and weight
    betsy_height = 71  # 5'11" converted to inches
    betsy_weight = 155
    # Define Nicole Kidman's height and weight
    nicole_height = 71
    nicole_weight = 137
    # Check if Nicole Kidman's height and weight are suitable for playing Psylocke
    if nicole_height == betsy_height and nicole_weight >= betsy_weight:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())