def solution():
    # Define the cost of the gaming PC and the sale price of the old video card
    pc_cost = 1200
    old_card_sale_price = 300
    
    # Calculate the total cost of the video card replacement
    new_card_cost = 500
    total_card_cost = new_card_cost - old_card_sale_price
    
    # Calculate the total cost of the gaming PC after the video card replacement
    total_cost_with_card = pc_cost + total_card_cost
    
    result = total_cost_with_card
    return result

print(solution())