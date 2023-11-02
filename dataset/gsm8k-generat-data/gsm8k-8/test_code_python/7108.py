def solution():
    # Calculate the number of jumps Bobby can do in one minute as an adult
    adult_jumps_per_minute = 60

    # Calculate the difference between adult jumps per minute and child jumps per minute
    difference = adult_jumps_per_minute - 30

    # Calculate the total number of additional jumps Bobby can do in one minute as an adult
    additional_jumps_per_minute = difference

    # Calculate the total number of additional jumps Bobby can do in one hour
    additional_jumps_per_hour = additional_jumps_per_minute * 60

    result = additional_jumps_per_hour
    return result

print(solution())