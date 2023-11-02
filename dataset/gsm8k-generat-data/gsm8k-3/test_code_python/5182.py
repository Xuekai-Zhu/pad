def solution():
    """While at Wizards Park, Kate buys 3 magic wands, one for herself and two for her friends. When she returns she sells the wands to her friends for $5 more than she paid. If she collected $130 after the sale, how much money did each wand cost?"""
    # Define the number of wands bought and the extra amount sold for
    NUM_WANDS = 3
    EXTRA_AMOUNT = 5

    # Define the total amount collected after the sale
    total_collected = 130

    # Calculate the cost per wand
    cost_per_wand = (total_collected - NUM_WANDS * EXTRA_AMOUNT) / NUM_WANDS

    # Display the cost per wand
    result = cost_per_wand
    return result

print(solution())