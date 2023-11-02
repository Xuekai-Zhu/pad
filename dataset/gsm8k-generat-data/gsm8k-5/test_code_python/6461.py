def solution():
    john_money = 200  # John had $200
    mother_money = (3/8) * john_money  # John gave 3/8 of his money to his mother
    father_money = (3/10) * john_money  # John gave 3/10 of his money to his father
    total_given_money = mother_money + father_money  # Total money given away by John
    remaining_money = john_money - total_given_money  # John's remaining money

    result = remaining_money
    return result

print(solution())