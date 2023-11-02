def solution():
    # Define the variables
    adult_price = 15
    child_price = 8
    total_price = 720
    # Let c be the number of children
    # Then, the number of adults = c + 25
    c = (total_price - (c + 25) * adult_price)/ (child_price - adult_price)
    # Convert c to an integer since it represents the number of children
    c = int(c)
    result = c
    return result

print(solution())