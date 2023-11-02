def solution():
    total_time = 60  # The car took 60 hours to travel from Ngapara to Zipra
    time_ratio = 0.8  # The car traveled from Ningi to Zipra in 80% of the time it traveled from Ngapara to Zipra

    # Calculate the time the car traveled from Ningi to Zipra
    ningi_to_zipra_time = total_time * time_ratio

    # Calculate the total time the car traveled that day
    total_travel_time = ningi_to_zipra_time + total_time
    result = total_travel_time
    return result

print(solution())