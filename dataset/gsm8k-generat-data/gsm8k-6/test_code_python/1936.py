def solution():
    # Calculate the total amount of money in the pot
    total_money = 8 * 5  # Josh and his 7 friends each put in $5

    # Calculate the amount of money for first place
    first_place_money = 0.8 * total_money

    # Calculate the amount of money remaining after first place
    remaining_money = total_money - first_place_money

    # Calculate the amount of money for second and third place
    second_and_third_place_money = remaining_money / 2

    # Calculate the amount of money for third place
    third_place_money = second_and_third_place_money

    result = third_place_money
    return result

print(solution())