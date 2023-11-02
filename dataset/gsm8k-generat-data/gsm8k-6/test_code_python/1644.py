def solution():
    # Calculate the total number of pictures taken by John in 3 years
    total_pictures = 10 * 365 * 3  
    
    # Calculate the number of memory cards needed to store all the pictures
    memory_cards = total_pictures // 50 + 1  
    
    # Calculate the total cost of the memory cards
    total_cost = memory_cards * 60  
    
    result = total_cost
    return result

print(solution())