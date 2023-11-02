def solution():
    """Troy is thinking of buying a new computer that is worth $80. He has initially saved $50 and plans to sell his old computer for $20. How much more money does he need so he could buy the new computer?"""
    new_computer_cost = 80
    initial_savings = 50
    old_computer_sale = 20
    remaining_cost = new_computer_cost - initial_savings + old_computer_sale
    result = remaining_cost
    return result

print(solution())