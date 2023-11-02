def solution():
    # Define the number of Anna's pencils
    anna_pencils = 50

    # Calculate the number of Harry's pencils
    harry_pencils = 2 * anna_pencils

    # Calculate the number of pencils Harry has left after losing 19
    harry_pencils_left = harry_pencils - 19

    result = harry_pencils_left
    return result

print(solution())