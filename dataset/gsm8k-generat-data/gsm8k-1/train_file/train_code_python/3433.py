def solution():
    """Lucy had a 500g bag of flour in the cupboard at the start of the week. She used 240g when she baked cookies on Tuesday, and accidentally spilled half of what was left when she was putting the flour away. If Lucy wants a full bag of flour in the cupboard, how much flour does she need to buy, in grams?"""
    initial_flour = 500
    used_flour = 240
    spilled_flour = (initial_flour - used_flour) / 2
    total_flour = initial_flour - used_flour - spilled_flour
    flour_needed = initial_flour - total_flour
    result = flour_needed
    return result

print(solution())