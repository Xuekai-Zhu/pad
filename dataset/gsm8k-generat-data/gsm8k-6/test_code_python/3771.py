def solution():
    # Calculate the total number of seats in Section A
    total_seats_A = 60 + 3*80  # 1 subsection with 60 seats and 3 subsections with 80 seats each

    # Calculate the number of seats in Section B
    seats_B = 3*total_seats_A + 20  # 3 times as many seats as Section A has total, plus 20 more seats

    result = seats_B
    return result

print(solution())