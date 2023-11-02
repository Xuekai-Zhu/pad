def solution():
    people_per_row = 8
    total_rows = 12
    seats_available = people_per_row * total_rows * (3/4)
    seats_not_available = people_per_row * total_rows - seats_available
    result = seats_not_available
    return result

print(solution())