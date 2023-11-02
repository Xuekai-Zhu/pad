def solution():
    """Page collects fancy shoes and has 80 pairs in her closet. She decides to donate 30% of her collection that she no longer wears. After dropping off her donation, she treats herself and buys 6 more pairs to add to her collection. How many shoes does she have now?"""
    
    # Define the initial number of shoes
    initial_shoes = 80
    
    # Calculate the number of shoes to be donated
    donate = 0.3 * initial_shoes
    
    # Calculate the remaining number of shoes
    remaining = initial_shoes - donate
    
    # Calculate the new total number of shoes after buying 6 more pairs
    new_total = remaining + 6
    
    result = new_total
    return result

print(solution())