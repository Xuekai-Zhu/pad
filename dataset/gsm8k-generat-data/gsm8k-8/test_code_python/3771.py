def solution():
    # Calculate the total seats in Section A
    section_a_total_seats = 60 + 3 * 80

    # Calculate the total seats in Section B
    section_b_total_seats = 3 * section_a_total_seats + 20

    result = section_b_total_seats
    return result

print(solution())