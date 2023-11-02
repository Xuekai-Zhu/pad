def solution():
    num_people = 84
    num_cars = 7
    num_seats_per_car = 2

    # Calculate the total number of seats on the roller coaster
    total_seats = num_cars * num_seats_per_car

    # Calculate the number of times the roller coaster must run
    num_runs = num_people // total_seats
    if num_people % total_seats != 0:
        num_runs += 1
    
    result = num_runs
    return result

print(solution())