def solution():
    found_money = 12
    friend_money = 1
    watch_cost = 20

    # Calculate the total amount of money Evan has, including the money from David
    total_money = found_money + friend_money

    # Calculate the amount of money Evan still needs to buy the watch
    money_needed = watch_cost - total_money
    result = money_needed
    return result

print(solution())