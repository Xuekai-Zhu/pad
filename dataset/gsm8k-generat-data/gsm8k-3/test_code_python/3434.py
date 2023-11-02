def solution():
    """Lucy has been trying new recipes and wants to make sure she keeps the cupboard stocked with ingredients. She had a 500g bag of flour in the cupboard at the start of the week. She used 240g when she baked cookies on Tuesday, and accidentally spilled half of what was left when she was putting the flour away. If Lucy wants a full bag of flour in the cupboard, how much flour does she need to buy, in grams?"""
    # Initialize the amount of flour left in the cupboard
    flour_left = 500 - 240   # Lucy used 240g for baking cookies on Tuesday
    
    # Calculate the amount of flour spilled when putting flour away
    flour_spilled = flour_left / 2
    
    # Calculate the total amount of flour currently in the cupboard
    total_flour = flour_left - flour_spilled
    
    # Calculate the amount of flour Lucy needs to buy to have a full bag
    flour_needed = 500 - total_flour
    
    # Display the amount of flour needed to buy
    result = flour_needed
    return result

print(solution())