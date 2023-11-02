def solution():
    # Calculate the total number of seats in Section A
    total_seats_A = 60 + (3 * 80)

    # Calculate the number of seats in Section B based on Section A
    total_seats_B = (3 * total_seats_A) + 20

    result = total_seats_B
    return result

print(solution())