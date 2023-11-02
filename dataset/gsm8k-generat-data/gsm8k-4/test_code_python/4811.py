def solution():
    """There are 100 people in a theater. If 19 of these people have blue eyes, half of them have brown eyes, a quarter have black eyes, and the rest have green eyes, how many of them have green eyes?"""
    # Define the total number of people in the theater
    total_people = 100

    # Calculate the number of people with blue eyes
    blue_eyes = 19

    # Calculate the number of people with brown eyes
    brown_eyes = total_people / 2

    # Calculate the number of people with black eyes
    black_eyes = total_people / 4

    # Calculate the number of people with green eyes
    green_eyes = total_people - blue_eyes - brown_eyes - black_eyes

    # Return the result
    result = green_eyes
    return result

print(solution())