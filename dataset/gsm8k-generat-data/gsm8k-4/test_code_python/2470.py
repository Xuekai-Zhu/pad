def solution():
    """David and Brenda are playing Scrabble. Brenda is ahead by 22 points when she makes a 15-point play. David responds with a 32-point play. By how many points is Brenda now ahead?"""
    # Define the initial point difference between Brenda and David
    point_difference = 22

    # Update the point difference after Brenda's play
    point_difference += 15

    # Update the point difference after David's play
    point_difference -= 32

    # Calculate the final point difference between Brenda and David
    final_point_difference = point_difference

    # Return the result
    result = final_point_difference
    return result

print(solution())