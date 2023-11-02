def solution():
    # Calculate the total number of times John sneezes
    sneezes_per_second = 1 / 3  # John sneezes once every 3 seconds
    sneezes_per_minute = sneezes_per_second * 60  # number of sneezes per minute
    total_sneezes = int(sneezes_per_minute * 2)  # sneezing fit lasts for 2 minutes
    result = total_sneezes
    return result

print(solution())