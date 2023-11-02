def solution():
    # Calculate the amount of money John gives to Jenna
    jenna_money = 100 * (1/4)

    # Calculate the amount of money John has left after buying groceries
    remaining_money = 100 - jenna_money - 40
    result = remaining_money
    return result

print(solution())