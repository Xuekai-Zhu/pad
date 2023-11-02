def solution():
    """Dave bought 3 packs of white T-shirts and 2 packs of blue T-shirts for his basketball team. The white T-shirts come in packs of 6, and the blue T-shirts come in packs of 4. How many T-shirts did Dave buy in all?"""
    # Define the number of T-shirts in each pack
    WHITE_PACK_SIZE = 6
    BLUE_PACK_SIZE = 4

    # Define the number of packs bought
    white_packs = 3
    blue_packs = 2

    # Calculate the total number of white T-shirts bought
    white_shirts = white_packs * WHITE_PACK_SIZE

    # Calculate the total number of blue T-shirts bought
    blue_shirts = blue_packs * BLUE_PACK_SIZE

    # Calculate the total number of T-shirts bought
    total_shirts = white_shirts + blue_shirts

    # Display the total number of T-shirts
    result = total_shirts
    return result

print(solution())