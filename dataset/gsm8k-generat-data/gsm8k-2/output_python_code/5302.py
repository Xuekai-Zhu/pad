def solution():
    """On a particular day, a car traveled from Ningi to Zipra in 80% of the time it traveled from Ngapara to Zipra. If the car took 60 hours to travel from Ngapara to Zipra, calculate the total time the car traveled that day."""
    ngapara_zipra_time = 60
    ningi_zipra_time = 0.8 * ngapara_zipra_time
    total_time = ngapara_zipra_time + ningi_zipra_time
    result = total_time
    return result

print(solution())