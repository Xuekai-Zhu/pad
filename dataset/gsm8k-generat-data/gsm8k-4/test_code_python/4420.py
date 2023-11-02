def solution():
    """Steve has 2 boxes of pencils with 12 pencils in each box. He gave Matt 3 more pencils than he gave to Lauren. If Steve gave 6 pencils to Lauren, how many pencils does he have left?"""
    # Define the number of pencils per box and the total number of boxes
    PENCILS_PER_BOX = 12
    NUM_BOXES = 2

    # Calculate the total number of pencils Steve has
    total_pencils = PENCILS_PER_BOX * NUM_BOXES

    # Calculate the number of pencils Steve gave to Matt
    matt_pencils = 6 + 3

    # Calculate the total number of pencils Steve gave away
    total_given_away = 6 + matt_pencils

    # Calculate the number of pencils Steve has left
    pencils_left = total_pencils - total_given_away

    # Return the result
    result = pencils_left
    return result

print(solution())