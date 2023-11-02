def solution():
    """Mr. Llesis had 50 kilograms of rice. He kept 7/10 of it in storage and gave the rest to Mr. Everest. How many kilograms of rice did Mr. Llesis keep than Mr. Everest?"""
    total_rice = 50
    storage_rice = 7/10 * total_rice
    everest_rice = total_rice - storage_rice
    difference = storage_rice - everest_rice
    result = difference
    return result

print(solution())