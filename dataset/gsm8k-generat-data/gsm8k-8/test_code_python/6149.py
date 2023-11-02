def solution():
    # Define the weight of one bag of chips and one tin of cookies in pounds
    chip_weight = 20 / 16
    cookie_weight = 9 / 16

    # Calculate the total weight in pounds
    total_weight = 6 * chip_weight + 4 * cookie_weight

    # Round the total weight to two decimal places
    total_weight = round(total_weight, 2)
    result = total_weight
    return result

print(solution())