def solution():
    # Calculate the number of items needed to fill each display
    necklaces_needed = 12 - 5
    rings_needed = 30 - 18
    bracelets_needed = 15 - 8
    
    # Calculate the total cost of filling the displays
    total_cost = (necklaces_needed * 4) + (rings_needed * 10) + (bracelets_needed * 5)
    result = total_cost
    return result

print(solution())