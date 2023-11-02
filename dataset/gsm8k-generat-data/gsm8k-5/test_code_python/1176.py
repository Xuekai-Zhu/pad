def solution():
    num_go_karts = 1  # Paula wants to ride the go-karts 1 time
    num_bumper_cars = 4  # Paula wants to ride the bumper cars 4 times
    cost_go_karts = 4  # It costs 4 tickets to ride the go-karts
    cost_bumper_cars = 5  # It costs 5 tickets to ride the bumper cars

    # Calculate the total number of tickets needed
    total_tickets = (num_go_karts * cost_go_karts) + (num_bumper_cars * cost_bumper_cars)
    result = total_tickets
    return result

print(solution())