def solution():
    """When Nathan is cold, he adds an extra blanket to his bed. Each blanket warms him up by 3 degrees. One night, he was cold enough that he added half of the 14 blankets in his closet on his bed. How many degrees did the blankets warm Nathan up?"""
    # Define the warming effect of each blanket
    WARMING_EFFECT = 3

    # Calculate the number of blankets Nathan added to his bed
    blankets_added = 14 * 0.5

    # Calculate the total warming effect of the blankets
    total_warming_effect = blankets_added * WARMING_EFFECT

    # Return the total warming effect
    result = total_warming_effect
    return result

print(solution())