def solution():
    cast_cost = 200  # The doctor charges her $200 for the cast
    visit_cost = 300 * 60  # The doctor charges her $300 per hour for a 30-minute visit
    pill_cost = 4 * 30  # The doctor charges $4/pill for 30 painkillers
    parking_cost = 6 * 2  # The doctor charges the doctor for a mandatory minimum of 2 hours of parking

    # Calculate the total cost of the doctor's visit
    total_cost = cast_cost + visit_cost + painkiller_cost + parking_cost
    result = total_cost
    return result

print(solution())