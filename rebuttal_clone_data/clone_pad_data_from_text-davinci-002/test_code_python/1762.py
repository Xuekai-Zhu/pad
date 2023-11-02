def solution():
    valid_tickets = 300 * (75/100)
    permanent_passes = valid_tickets / 5
    total_cars = valid_tickets + permanent_passes
    result = total_cars - 300
    return result

print(solution())