def solution():
    # Calculate the total number of pieces in all puzzles
    total_pieces = 8 * 300 + 5 * 500

    # Calculate the total time Pablo needs to complete all puzzles
    total_time = total_pieces / 100

    # Calculate the number of days Pablo can work on puzzles for a maximum of 7 hours each day
    max_work_hours = 7
    max_work_time = max_work_hours * 60
    total_days = total_time / max_work_time

    result = total_days
    return result

print(solution())