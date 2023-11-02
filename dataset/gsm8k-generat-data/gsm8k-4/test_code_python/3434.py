def solution():
    """Lucy has been trying new recipes and wants to make sure she keeps the cupboard stocked with ingredients. 
    She had a 500g bag of flour in the cupboard at the start of the week. She used 240g when she baked cookies on Tuesday, 
    and accidentally spilled half of what was left when she was putting the flour away. 
    If Lucy wants a full bag of flour in the cupboard, how much flour does she need to buy, in grams?"""
    
    # Define the amount of flour that Lucy had at the start of the week
    initial_flour = 500

    # Calculate the amount of flour that Lucy had left after baking cookies
    remaining_flour = initial_flour - 240

    # Calculate the amount of flour that Lucy had left after spilling half
    final_flour = remaining_flour / 2

    # Calculate the amount of flour that Lucy needs to buy to have a full bag
    needed_flour = 500 - final_flour

    result = needed_flour
    return result

print(solution())