def solution():
    # Define the time it took to travel from Ngapara to Zipra
    ngapara_to_zipra_time = 60

    # Calculate the time it took to travel from Ningi to Zipra
    ningi_to_zipra_time = 0.8 * ngapara_to_zipra_time

    # Calculate the total time the car traveled that day
    total_time = ngapara_to_zipra_time + ningi_to_zipra_time
    result = total_time
    return result

print(solution())