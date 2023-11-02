def solution():
    """On Tuesday, Max's mom gave him $8 dollars for a hot dog at the Grand Boulevard park. On Wednesday, his mom gave him 5 times as much money as she gave him on Tuesday. On Thursday, his mom gave him $9 more in money than she gave him on Wednesday. How much more money did his mom give him on Thursday than she gave him on Tuesday?"""
    tuesday_money = 8
    wednesday_money = tuesday_money * 5
    thursday_money = wednesday_money + 9
    difference = thursday_money - tuesday_money
    result = difference
    return result

print(solution())