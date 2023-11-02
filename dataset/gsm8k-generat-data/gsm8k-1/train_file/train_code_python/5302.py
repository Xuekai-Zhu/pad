def solution():
    """On a particular day, a car traveled from Ningi to Zipra in 80% of the time it traveled from Ngapara to Zipra. If the car took 60 hours to travel from Ngapara to Zipra, calculate the total time the car traveled that day."""
    ngapara_to_zipra_time = 60
    ningi_to_zipra_time = ngapara_to_zipra_time * 0.8 # 80% of the time for Ngapara to Zipra
    total_time = ngapara_to_zipra_time + ningi_to_zipra_time
    result = total_time
    return result

print(solution())