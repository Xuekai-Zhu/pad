def solution():
    """Luther made 12 pancakes for breakfast. His family has 8 people. How many more pancakes must he make for everyone to have a second pancake?"""
    total_pancakes = 12
    total_people = 8
    current_pancakes_per_person = total_pancakes / total_people
    remaining_pancakes_needed = (current_pancakes_per_person * 2 - 1) * total_people - total_pancakes
    result = remaining_pancakes_needed
    return result

print(solution())