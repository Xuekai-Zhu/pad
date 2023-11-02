def solution():
    # Calculate the total number of pencils that Steve gave away
    total_given_away = 6 + (6 + 3)  # Steve gave 6 pencils to Lauren and 3 more to Matt

    # Calculate the total number of pencils Steve has left
    total_pencils = 2 * 12  # Steve has 2 boxes of pencils with 12 pencils in each box
    pencils_left = total_pencils - total_given_away

    result = pencils_left
    return result

print(solution())