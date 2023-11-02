def solution():
    """Luther made 12 pancakes for breakfast. His family has 8 people. How many more pancakes must he make for everyone to have a second pancake?"""
    # Calculate the total number of pancakes needed for everyone to have 2 pancakes
    total_pancakes_needed = 8 * 2

    # Calculate the number of pancakes Luther has already made
    pancakes_made = 12

    # Calculate the number of additional pancakes needed
    additional_pancakes_needed = total_pancakes_needed - pancakes_made

    # Display the number of additional pancakes needed
    result = additional_pancakes_needed
    return result

print(solution())