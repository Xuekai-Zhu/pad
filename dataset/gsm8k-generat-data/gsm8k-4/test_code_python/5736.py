def solution():
    """Ashton had two boxes of pencils with fourteen pencils in each box. He gave six pencils to his brother. How many pencils did Ashton have left?"""
    # Define the total number of pencils before giving any away
    initial_pencils = 2 * 14

    # Define the number of pencils given away
    given_away = 6

    # Calculate the number of pencils left
    pencils_left = initial_pencils - given_away

    # return the result
    result = pencils_left
    return result

print(solution())