def solution():
    """ Luther made 12 pancakes for breakfast. His family has 8 people. How many more pancakes must he make for everyone to have a second pancake? """
    total_pancakes = 12
    people = 8
    pancakes_per_person = 2
    needed_pancakes = (people * pancakes_per_person) - total_pancakes
    result = needed_pancakes
    return result

print(solution())