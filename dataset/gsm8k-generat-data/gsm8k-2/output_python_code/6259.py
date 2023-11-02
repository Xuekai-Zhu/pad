def solution():
    """Sandra wants to buy some sweets. She saved $10 for this purpose. Her mother gave her an additional $4, and her father twice as much as her mother. One candy costs $0.5, and one jelly bean $0.2. She wants to buy 14 candies and 20 jelly beans. How much money will she be left with after the purchase?"""
    sandra_money = 10
    mother_money = 4
    father_money = 2 * mother_money
    total_money = sandra_money + mother_money + father_money
    candy_cost = 0.5
    jelly_bean_cost = 0.2
    total_candy_cost = 14 * candy_cost
    total_jelly_bean_cost = 20 * jelly_bean_cost
    total_purchase_cost = total_candy_cost + total_jelly_bean_cost
    money_left = total_money - total_purchase_cost
    result = money_left
    return result

print(solution())