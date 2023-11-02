def solution():
    """Steve has 2 boxes of pencils with 12 pencils in each box. He gave Matt 3 more pencils than he gave to Lauren. If Steve gave 6 pencils to Lauren, how many pencils does he have left?"""
    # Define the number of boxes and pencils per box
    BOXES = 2
    PENCILS_PER_BOX = 12

    # Calculate the total number of pencils Steve has
    total_pencils = BOXES * PENCILS_PER_BOX

    # Calculate the number of pencils Steve gave to Matt
    matt_pencils = 6 + 3

    # Calculate the number of pencils Steve gave to Lauren
    lauren_pencils = 6

    # Calculate the total number of pencils given away
    given_pencils = matt_pencils + lauren_pencils

    # Calculate the number of pencils Steve has left
    remaining_pencils = total_pencils - given_pencils

    # Display the number of pencils Steve has left
    result = remaining_pencils
    return result

print(solution())