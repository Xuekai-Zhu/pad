def solution():
    total_seats = 150 * 10  # There are 150 rows with 10 seats each
    seats_taken = 0.8 * total_seats  # 20% of seats were not taken, so 80% were taken
    revenue = seats_taken * 10  # Each ticket costs $10
    result = revenue
    return result

print(solution())