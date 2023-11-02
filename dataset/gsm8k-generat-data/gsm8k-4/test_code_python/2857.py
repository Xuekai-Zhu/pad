def solution():
    """Dave bought 3 packs of white T-shirts and 2 packs of blue T-shirts for his basketball team. The white T-shirts come in packs of 6, and the blue T-shirts come in packs of 4. How many T-shirts did Dave buy in all?"""
    # Define the number of packs of white and blue T-shirts
    white_packs = 3
    blue_packs = 2

    # Calculate the number of white and blue T-shirts
    white_shirts = white_packs * 6
    blue_shirts = blue_packs * 4

    # Calculate the total number of T-shirts
    total_shirts = white_shirts + blue_shirts

    # return the result
    result = total_shirts
    return result

print(solution())