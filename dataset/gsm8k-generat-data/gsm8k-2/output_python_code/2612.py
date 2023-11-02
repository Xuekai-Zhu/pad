def solution():
    """Tony has $87. He needs to buy some cheese, which costs $7 a pound and a pound of beef that costs $5 a pound. After buying the beef and his cheese, he has $61 left. How many pounds of cheese did he buy?"""
    total_money = 87
    beef_price = 5
    cheese_price = 7
    remaining_money = 61
    beef_weight = 1
    total_weight = 0
    while True:
        cheese_weight = (total_money - remaining_money - (beef_price * beef_weight)) // cheese_price
        if cheese_weight <= 0:
            break
        weight = cheese_weight + beef_weight
        total_weight += weight
        beef_weight += 1

    result = total_weight
    return result

print(solution())