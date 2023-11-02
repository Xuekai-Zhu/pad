def solution():
    """Luther made 12 pancakes for breakfast. His family has 8 people. How many more pancakes must he make for everyone to have a second pancake?"""
    # Define the number of pancakes Luther made and the number of people in his family
    pancakes = 12
    family_members = 8

    # Calculate the total number of pancakes needed for everyone to have a second pancake
    total_pancakes_needed = 2 * family_members

    # Calculate the number of additional pancakes needed
    additional_pancakes_needed = total_pancakes_needed - pancakes

    # Display the result
    result = additional_pancakes_needed
    return result

print(solution())