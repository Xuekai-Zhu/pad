def solution():
    """John is working as an IT specialist. He repairs broken computers. One day he had to fix 20 computers. 20% of them were unfixable, and 40% of them needed to wait a few days for spare parts to come. The rest John was able to fix right away. How many computers John was able to fix right away?"""
    # Define the total number of computers
    total_computers = 20

    # Calculate the number of unfixable computers
    unfixable = total_computers * 0.2

    # Calculate the number of computers that need spare parts
    parts_needed = total_computers * 0.4

    # Calculate the number of computers that can be fixed right away
    fixed_right_away = total_computers - unfixable - parts_needed

    # Return the result
    result = fixed_right_away
    return result

print(solution())