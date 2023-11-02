def solution():
    """Haleigh needs to buy leggings for her pet animals. She has 4 dogs and 3 cats. How many pairs of leggings does she need?"""
    # Calculate the total number of legs
    total_legs = 4 * 4 + 3 * 4  # 4 legs per dog, 4 legs per cat

    # Calculate the number of pairs of leggings needed
    num_leggings = total_legs // 2  # Each pair of leggings covers 2 legs

    # Display the number of pairs of leggings needed
    result = num_leggings
    return result

print(solution())