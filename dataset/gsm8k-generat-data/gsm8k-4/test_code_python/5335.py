def solution():
    """On Tuesday, Max's mom gave him $8 dollars for a hot dog at the Grand Boulevard park. On Wednesday, his mom gave him 5 times as much money as she gave him on Tuesday. On Thursday, his mom gave him $9 more in money than she gave him on Wednesday. How much more money did his mom give him on Thursday than she gave him on Tuesday?"""
    # Define the amount of money given on Tuesday
    tuesday_money = 8

    # Define the amount of money given on Wednesday
    wednesday_money = 5 * tuesday_money

    # Define the amount of money given on Thursday
    thursday_money = wednesday_money + 9

    # Calculate the difference in money between Tuesday and Thursday
    difference = thursday_money - tuesday_money

    # return the result
    result = difference
    return result

print(solution())