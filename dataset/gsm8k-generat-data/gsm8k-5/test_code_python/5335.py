def solution():
    # Calculate the amount of money Max's mom gave him on Tuesday
    tuesday_money = 8

    # Calculate the amount of money Max's mom gave him on Wednesday
    wednesday_money = 5 * tuesday_money

    # Calculate the amount of money Max's mom gave him on Thursday
    thursday_money = wednesday_money + 9

    # Calculate the difference between the amount of money Max's mom gave him on Thursday and Tuesday
    difference = thursday_money - tuesday_money
    result = difference
    return result

print(solution())