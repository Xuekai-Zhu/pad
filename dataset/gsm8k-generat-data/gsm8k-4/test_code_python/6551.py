def solution():
    """Troy is thinking of buying a new computer that is worth $80. He has initially saved $50 and plans to sell his old computer for $20. How much more money does he need so he could buy the new computer?"""
    # Define the cost of the new computer, Troy's initial savings, and the amount he will get from selling his old computer
    new_comp_cost = 80
    initial_savings = 50
    old_comp_sale = 20

    # Calculate the remaining amount Troy needs to buy the new computer
    remaining_amount = new_comp_cost - initial_savings - old_comp_sale

    # Display the remaining amount needed
    result = remaining_amount
    return result

print(solution())