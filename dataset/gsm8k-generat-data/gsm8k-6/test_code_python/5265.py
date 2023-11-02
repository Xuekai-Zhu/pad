def solution():
    # Calculate the total number of chocolates Wendy can package in 4 hours
    chocolates_per_minute = (2 * 12) / 5  # Wendy can package 2 dozen (24) chocolates in 5 minutes
    chocolates_per_hour = chocolates_per_minute * 60  # the number of chocolates Wendy can package in an hour
    total_chocolates = chocolates_per_hour * 4  # the number of chocolates Wendy can package in 4 hours
    result = total_chocolates
    return result

print(solution())