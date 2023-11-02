def solution():
    # Calculate the time it takes Eric to get to the park
    time_to_park = 20/60 + 10/60  # convert minutes to hours

    # Calculate the time it takes Eric to return home
    time_return_home = 3 * time_to_park
    
    result = time_return_home
    return result

print(solution())