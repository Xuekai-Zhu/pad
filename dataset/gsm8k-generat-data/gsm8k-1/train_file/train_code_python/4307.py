def solution():
    """John goes to the bakery to buy rolls. They sell them for 5 dollars for a dozen. He spent 15 dollars. How many rolls did he get?"""
    cost_per_dozen = 5
    total_cost = 15
    dozens_purchased = total_cost // cost_per_dozen
    rolls_purchased = dozens_purchased * 12
    result = rolls_purchased
    return result

print(solution())