def solution():
    """Sandra wants to buy some sweets. She saved $10 for this purpose. Her mother gave her an additional $4, and her father twice as much as her mother. One candy costs $0.5, and one jelly bean $0.2. She wants to buy 14 candies and 20 jelly beans. How much money will she be left with after the purchase?"""
    sandra_money = 10
    mother_money = 4
    father_money = 2 * mother_money
    candy_price = 0.5
    jellybean_price = 0.2
    candies_bought = 14
    jellybeans_bought = 20
    
    total_cost = (candies_bought * candy_price) + (jellybeans_bought * jellybean_price)
    total_money = sandra_money + mother_money + father_money
    
    money_left = total_money - total_cost
    result = money_left
    
    return result

print(solution())