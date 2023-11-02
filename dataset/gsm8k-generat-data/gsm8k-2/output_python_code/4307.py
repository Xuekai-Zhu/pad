def solution():
    """John goes to the bakery to buy rolls. They sell them for 5 dollars for a dozen. He spent 15 dollars. How many rolls did he get?"""
    cost_per_dozen = 5
    total_cost = 15
    rolls_per_dozen = 12
    dozens_purchased = total_cost / cost_per_dozen
    rolls_purchased = dozens_purchased * rolls_per_dozen
    result = rolls_purchased
    return result

print(solution())