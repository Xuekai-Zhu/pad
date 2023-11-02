def solution():
    sneezing_time = 2 * 60  # Convert 2 minutes to seconds
    sneezes_per_second = 1 / 3  # John sneezes once every 3 seconds

    # Calculate the total number of sneezes
    total_sneezes = sneezes_per_second * sneezing_time
    result = total_sneezes
    return result

print(solution())