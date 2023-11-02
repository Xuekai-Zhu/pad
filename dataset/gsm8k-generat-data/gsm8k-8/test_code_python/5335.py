def solution():
    # Calculate the amount of money given on Wednesday
    wednesday_money = 8 * 5

    # Calculate the amount of money given on Thursday
    thursday_money = wednesday_money + 9

    # Calculate the difference between Thursday and Tuesday's money
    difference = thursday_money - 8

    result = difference
    return result

print(solution())