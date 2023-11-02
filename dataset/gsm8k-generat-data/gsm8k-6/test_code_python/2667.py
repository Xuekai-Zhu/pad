def solution():
    # Calculate the amount of money Zachary received from selling his video games
    zachary_money = 40 * 5

    # Calculate the amount of money Jason received from selling his video games
    jason_money = zachary_money * 1.3

    # Calculate the amount of money Ryan received from selling his video games
    ryan_money = jason_money + 50

    # Calculate the total amount of money the three friends received together from selling their video games
    total_money = zachary_money + jason_money + ryan_money
    result = total_money
    return result

print(solution())