def solution():
    # Calculate the number of jewels the dragon owned before the king stole three prize jewels
    # Let x be the original number of jewels
    # x - 3 = 2/3 * x (since the new jewels are a third of the original number)
    # 3x - 9 = 2x
    # x = 9
    original_jewels = 9

    # Calculate the number of jewels the dragon owned in the end
    # The dragon stole twice as many jewels as the king had on his crown
    # Let y be the number of jewels on the king's crown
    # 2y + 3 = 9 (since the dragon stole three prize jewels)
    # 2y = 6
    # y = 3
    crown_jewels = 3
    total_jewels = original_jewels + crown_jewels * 2

    result = total_jewels
    return result

print(solution())