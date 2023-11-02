def solution():
    pancakes_per_person = 1  # Each person has had 1 pancake already
    total_people = 8  # Luther's family has 8 people
    current_pancakes = 12  # Luther made 12 pancakes for breakfast

    # Calculate the total number of pancakes needed for everyone to have a second pancake
    total_pancakes_needed = (pancakes_per_person * total_people * 2) - current_pancakes

    result = total_pancakes_needed
    return result

print(solution())