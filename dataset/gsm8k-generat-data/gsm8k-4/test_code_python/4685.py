def solution():
    """Mark had 10 pieces of fruit to eat in school this week. On Friday, he decided to keep 2 pieces of fruit for next week. He then brings the remaining 3 pieces of fruit to school for the day. How many pieces of fruit did Mark eat in the first four days of the week?"""
    # Define the total number of fruit Mark had at the beginning of the week
    initial_fruit = 10

    # Subtract the 2 pieces of fruit Mark kept for next week
    remaining_fruit = initial_fruit - 2

    # Subtract the 3 pieces of fruit Mark brought to school on Friday
    remaining_fruit -= 3

    # Determine how many pieces of fruit Mark ate in the first four days of the week
    eaten_fruit = remaining_fruit - 4

    # Return the result
    result = eaten_fruit
    return result

print(solution())