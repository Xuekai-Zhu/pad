def solution():
    """If Mr. Jones has 6 shirts for every pair of pants, and he has 40 pants, what's the total number of pieces of clothes he owns if all other factors remain the same?"""
    shirts_per_pants = 6
    pants_owned = 40
    total_shirts = shirts_per_pants * pants_owned
    total_clothes = total_shirts + pants_owned
    result = total_clothes
    return result

print(solution())