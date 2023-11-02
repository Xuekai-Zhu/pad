def solution():
    """Lily bought a Russian nesting doll as a souvenir. The biggest doll is 243 cm tall, and each doll is 2/3rd the size of the doll that contains it. How big is the 6th biggest doll?"""
    # Define the height of the biggest doll
    biggest_doll = 243

    # Initialize the height of the current doll to be the height of the biggest doll
    current_doll = biggest_doll

    # Loop through the dolls to find the height of the 6th biggest doll
    for i in range(1, 6):
        # Calculate the height of the next doll by multiplying the current doll's height by 2/3
        next_doll = current_doll * (2/3)

        # Set the current doll to be the next doll
        current_doll = next_doll

    # Round the height of the 6th biggest doll to the nearest 0.1 cm and return the result
    result = round(current_doll, 1)
    return result

print(solution())