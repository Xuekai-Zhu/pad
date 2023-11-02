def solution():
    # Calculate the total number of index cards needed
    total_cards = 10 * 30 * 6  # each student gets 10 cards, there are 30 students per class, and there are 6 periods a day
    
    # Calculate the total number of packs of index cards needed
    packs_needed = total_cards / 50
    
    # Calculate the total cost of the index cards
    total_cost = packs_needed * 3  # a 50 pack of index cards costs $3
    
    result = total_cost
    return result

print(solution())