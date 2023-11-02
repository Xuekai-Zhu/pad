def solution():
    # Calculate the total amount of money in the pot
    total_money = 8 * 5

    # Calculate the amount of money for first place
    first_place_money = total_money * 0.8

    # Calculate the amount of money left for second and third place
    second_and_third_money = total_money - first_place_money

    # Calculate the amount of money each for second and third place
    third_place_money = second_and_third_money / 2

    result = third_place_money
    return result

print(solution())