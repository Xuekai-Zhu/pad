def solution():
    time_to_wash_car = 10
    time_to_change_oil = 15
    time_to_change_tires = 30

    num_cars_washed = 9
    num_cars_oil_changed = 6
    num_sets_tires_changed = 2

    # Calculate the total time spent washing cars
    total_time_washing_cars = num_cars_washed * time_to_wash_car

    # Calculate the total time spent changing oil
    total_time_changing_oil = num_cars_oil_changed * time_to_change_oil

    # Calculate the total time spent changing tires
    total_time_changing_tires = num_sets_tires_changed * time_to_change_tires

    # Calculate the total time spent on all tasks
    total_time = total_time_washing_cars + total_time_changing_oil + total_time_changing_tires

    # Convert total time to hours
    total_hours = total_time / 60
    result = total_hours
    return result

print(solution())