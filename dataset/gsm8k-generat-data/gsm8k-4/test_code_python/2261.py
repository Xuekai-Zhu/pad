def solution():
    """Greg and Katie went to Mrs. Scarlet's gold store to have their gold chests opened. They realized Greg had four times less gold than Katie when Mrs. Scarlet opened the chests. If the total amount of gold is 100, how much gold does Greg have?"""
    # Define the total amount of gold as 100
    total_gold = 100

    # Calculate the amount of gold that Katie has
    katie_gold = total_gold / 5

    # Calculate the amount of gold that Greg has
    greg_gold = katie_gold / 4

    result = greg_gold
    return result

print(solution())