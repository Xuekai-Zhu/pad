def solution():
    """John decides to start collecting art. He pays the same price for his first 3 pieces of art and the total price came to $45,000. The next piece of art was 50% more expensive than those. How much did all the art cost?"""
    num_pieces = 4
    total_cost = 45000
    first_3_cost = total_cost / 3
    next_cost = first_3_cost * 1.5
    all_art_cost = total_cost + next_cost
    result = all_art_cost
    
    return result

print(solution())