def solution():
    """Greg and Katie went to Mrs. Scarlet's gold store to have their gold chests opened. They realized Greg had four times less gold than Katie when Mrs. Scarlet opened the chests. If the total amount of gold is 100, how much gold does Greg have?"""
    # Calculate the total amount of gold
    total_gold = 100

    # Calculate the gold ratio between Greg and Katie
    gold_ratio = 1 / 4

    # Calculate Katie's gold
    katie_gold = total_gold / (1 + gold_ratio)
    
    # Calculate Greg's gold
    greg_gold = katie_gold * gold_ratio

    # Display Greg's gold
    result = greg_gold
    return result

print(solution())