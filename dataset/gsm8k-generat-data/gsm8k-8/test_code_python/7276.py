def solution():
    # Define the number of apples and pears
    apples = x
    pears = x + 2

    # Define the number of bananas
    bananas = pears + 3

    # Calculate the total number of fruit
    total_fruit = apples + pears + bananas

    # Check if the total is 19 and return the number of bananas
    if total_fruit == 19:
        result = bananas
    else:
        result = "Error: Total number of fruit is not 19."
    return result

print(solution())