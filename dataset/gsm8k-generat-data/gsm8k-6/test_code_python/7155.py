def solution():
    # Calculate the total number of puzzle pieces Pablo has to put together
    total_pieces = 8 * 300 + 5 * 500

    # Calculate the total number of hours Pablo can work on puzzles each day
    max_hours = 7

    # Calculate the total number of hours Pablo needs to complete all the puzzles
    total_hours = total_pieces / 100

    # Calculate the number of days Pablo needs to complete all the puzzles
    days_needed = total_hours / max_hours

    result = days_needed
    return result

print(solution())