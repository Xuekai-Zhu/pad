def solution():
    """On a particular day, a car traveled from Ningi to Zipra in 80% of the time it traveled from Ngapara to Zipra. If the car took 60 hours to travel from Ngapara to Zipra, calculate the total time the car traveled that day."""
    # Define the time taken to travel from Ngapara to Zipra
    ngapara_to_zipra_time = 60
    
    # Calculate the time taken to travel from Ningi to Zipra
    ningi_to_zipra_time = ngapara_to_zipra_time * 0.8
    
    # Calculate the total time traveled
    total_time = ngapara_to_zipra_time + ningi_to_zipra_time
    
    # Display the total time
    result = total_time
    return result

print(solution())