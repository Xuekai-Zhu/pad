def solution():
    """Shonda is throwing an Easter egg hunt for her 2 kids and their 10 friends. She is also supplying enough eggs for herself and the 7 other adults there to find eggs as well. If there are 15 Easter egg baskets for everyone to share and each ends up holding 12 Easter eggs, when they equally distribute all of the Easter eggs to everyone, how many eggs does each person get?"""
    # Define the number of people at the Easter egg hunt
    num_people = 2 + 10 + 7

    # Calculate the total number of Easter eggs
    total_eggs = 15 * 12

    # Calculate the number of Easter eggs each person gets
    eggs_per_person = total_eggs // num_people

    # Display the number of Easter eggs each person gets
    result = eggs_per_person
    return result

print(solution())