def solution():
    cost_of_pc = 1200  # John buys a gaming PC for $1200
    selling_price_of_old_card = 300  # John sells the old video card for $300
    cost_of_new_card = 500  # John buys a new video card for $500

    # Calculate the net cost of the new video card after accounting for the sale of the old card
    net_cost_of_new_card = cost_of_new_card - selling_price_of_old_card

    # Calculate the total cost of the PC after replacing the video card
    total_cost = cost_of_pc + net_cost_of_new_card
    result = total_cost
    return result

print(solution())