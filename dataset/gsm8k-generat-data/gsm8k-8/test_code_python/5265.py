def solution():
    # Define the number of chocolates Wendy can package in one minute
    chocolates_per_minute = 2 * 12 / 5

    # Define the number of minutes in 4 hours
    minutes = 4 * 60

    # Calculate the total number of chocolates Wendy can package in 4 hours
    total_chocolates = chocolates_per_minute * minutes
    result = total_chocolates
    return result

print(solution())