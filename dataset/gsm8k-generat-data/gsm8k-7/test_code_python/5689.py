def solution():
    bunnies = 20
    burrow_frequency = 3
    minutes_per_hour = 60
    hours = 10
    
    # Calculate the total number of minutes in 10 hours
    total_minutes = minutes_per_hour * hours
    
    # Calculate the total number of times a single bunny comes out of its burrow in 10 hours
    bunny_total = burrow_frequency * total_minutes
    
    # Calculate the total number of times 20 bunnies come out of their burrows in 10 hours
    total_bunny_burrow = bunny_total * bunnies

    result = total_bunny_burrow
    return result

print(solution())