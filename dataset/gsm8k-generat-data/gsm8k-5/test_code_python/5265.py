def solution():
    chocolates_per_dozen = 12  # Wendy can package 2 dozen chocolates in 5 minutes
    minutes_per_hour = 60  # There are 60 minutes in one hour
    hours = 4  # Wendy works for 4 hours

    # Calculate the total number of chocolates Wendy can package in one minute
    chocolates_per_minute = (2 * chocolates_per_dozen) / 5
    # Calculate the total number of chocolates Wendy can package in one hour
    chocolates_per_hour = chocolates_per_minute * minutes_per_hour
    # Calculate the total number of chocolates Wendy can package in four hours
    total_chocolates = chocolates_per_hour * hours
    result = total_chocolates
    return result

print(solution())