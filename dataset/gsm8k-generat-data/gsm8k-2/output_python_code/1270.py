def solution():
    """Dorothy is 15 years old and wants to go to a museum with her family. Her family consists of her, her younger brother, her parents, and her grandfather. The regular ticket cost is $10. People 18 years old or younger have a discount of 30%. How much money will Dorothy have after this trip, when she currently has $70?"""
    num_tickets = 5
    regular_price = 10
    discounted_price = 0.7 * regular_price
    total_cost = num_tickets * (regular_price - discounted_price + discounted_price)
    remaining_money = 70 - total_cost
    result = remaining_money
    return result

print(solution())