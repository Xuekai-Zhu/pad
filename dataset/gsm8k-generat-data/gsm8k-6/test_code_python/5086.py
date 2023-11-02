def solution():
    # Calculate the cost of an evening ticket and a large popcorn & drink combo
    evening_ticket_cost = 10  
    combo_cost = 10  
    
    # Calculate the discounted cost of an afternoon ticket and combo
    afternoon_ticket_cost = evening_ticket_cost * 0.8  
    afternoon_combo_cost = combo_cost * 0.5  
    
    # Calculate the total cost of the evening movie experience and the discounted cost of the afternoon movie experience
    evening_total_cost = evening_ticket_cost + combo_cost 
    afternoon_total_cost = afternoon_ticket_cost + afternoon_combo_cost  
    
    # Calculate the amount saved by going to the earlier movie
    amount_saved = evening_total_cost - afternoon_total_cost  
    result = amount_saved
    return result

print(solution())