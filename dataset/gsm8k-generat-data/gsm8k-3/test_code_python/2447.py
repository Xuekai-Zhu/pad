def solution():
    """When Nathan is cold, he adds an extra blanket to his bed. Each blanket warms him up by 3 degrees. One night, he was cold enough that he added half of the 14 blankets in his closet on his bed. How many degrees did the blankets warm Nathan up?"""
    # Define the warming effect of each blanket
    BLANKET_WARMING = 3

    # Determine the number of blankets Nathan added to his bed
    blankets_added = 14 / 2

    # Calculate the total warming effect of the blankets
    total_warming = blankets_added * BLANKET_WARMING

    # Display the total warming effect
    result = total_warming
    return result

print(solution())