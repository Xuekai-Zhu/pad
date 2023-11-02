def solution():
    # Calculate the number of drinks in the pitcher
    num_drinks = 18 / (1/4 + 1 + 1/4)

    # Calculate the number of cups of lemonade in the pitcher
    cups_lemonade = num_drinks * 1.25

    result = cups_lemonade
    return result

print(solution())