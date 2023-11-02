def solution():
    """Sid takes $48 with him on a shopping trip to the mall. He spent some of his money on computer accessories and another $8 on snacks. After these purchases, he only has $4 more than half of his original money left. How much did he spend on computer accessories?"""
    original_money = 48
    snack_cost = 8
    remaining_money = (original_money - snack_cost) * 0.5 + 4
    computer_accessory_cost = original_money - snack_cost - remaining_money
    result = computer_accessory_cost
    return result

print(solution())