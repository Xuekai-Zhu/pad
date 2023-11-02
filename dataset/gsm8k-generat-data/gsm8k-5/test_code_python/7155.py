def solution():
    # Calculate the total number of pieces in all puzzles
    total_pieces = (8 * 300) + (5 * 500)

    # Calculate the total number of hours needed to complete all puzzles
    total_hours = total_pieces / 100

    # Calculate the number of days it will take to complete all puzzles
    days = total_hours / 7  # Assuming Pablo only works on puzzles for a maximum of 7 hours each day

    result = days
    return result

print(solution())