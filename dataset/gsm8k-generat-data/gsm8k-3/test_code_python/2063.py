def solution():
    """Bess can throw the Frisbee as far as 20 meters and she does this 4 times. Holly can only throw the Frisbee as far as 8 meters and she does this 5 times. Each time Bess throws a Frisbee, she throws it back to her original position. Holly leaves her Frisbee where it lands every time she throws it. In total, how many meters have the thrown Frisbees traveled?"""
    # Calculate the total distance Bess throws the Frisbee
    bess_distance = 20 * 4 * 2  # multiply by 2 because she throws it back to her original position

    # Calculate the total distance Holly throws the Frisbee
    holly_distance = 8 * 5

    # Calculate the total distance the Frisbees have traveled
    total_distance = bess_distance + holly_distance

    # Display the total distance
    result = total_distance
    return result

print(solution())