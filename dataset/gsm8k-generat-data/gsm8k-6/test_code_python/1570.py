def solution():
    # Calculate the total amount of chocolate milk Holly drank
    total_drink = 8 + 8 + 8 + 64 - 56  # she drinks 8 ounces with breakfast, 8 ounces during lunch break, 8 ounces with dinner and buys a new 64-ounce container but ends with 56 ounces
    initial_drink = total_drink + 56  # the initial amount of chocolate milk she had

    result = initial_drink
    return result

print(solution())