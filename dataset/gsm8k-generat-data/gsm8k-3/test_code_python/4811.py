def solution():
    """There are 100 people in a theater. If 19 of these people have blue eyes, half of them have brown eyes, a quarter have black eyes, and the rest have green eyes, how many of them have green eyes?"""
    # Define the number of people with each eye color
    blue = 19
    brown = 100 / 2
    black = 100 / 4

    # Calculate the number of people with green eyes
    green = 100 - blue - brown - black

    # Display the number of people with green eyes
    result = green
    return result

print(solution())