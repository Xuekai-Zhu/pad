def solution():
    # Calculate the amount of money Max's mom gave him on Wednesday
    wednesday_money = 8 * 5  # Max's mom gave him 5 times as much money as she gave him on Tuesday

    # Calculate the amount of money Max's mom gave him on Thursday
    thursday_money = wednesday_money + 9  # Max's mom gave him $9 more than she gave him on Wednesday

    # Calculate the difference in money between Tuesday and Thursday
    difference = thursday_money - 8  # Max's mom gave him $8 on Tuesday
    result = difference
    return result

print(solution())