def solution():
    # Calculate how much money Zachary made from selling his games
    zachary_money = 40 * 5

    # Calculate how much money Jason made from selling his games
    jason_money = zachary_money * 1.3

    # Calculate how much money Ryan made from selling his games
    ryan_money = jason_money + 50

    # Calculate the total amount of money the three friends received together
    total_money = zachary_money + jason_money + ryan_money
    result = total_money
    return result

print(solution())