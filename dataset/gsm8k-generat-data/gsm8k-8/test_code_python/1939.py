def solution():
    # Calculate Jerome's total money
    total_money = 2 * 43

    # Calculate how much Jerome gave to Bianca
    bianca_money = 3 * 8

    # Calculate the total amount Jerome gave away
    given_money = 8 + bianca_money

    # Calculate how much money Jerome has left
    remaining_money = total_money - given_money
    result = remaining_money
    return result

print(solution())