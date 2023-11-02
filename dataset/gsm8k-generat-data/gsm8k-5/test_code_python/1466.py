def solution():
    barks_per_minute = 30  # One dog barks 30 times per minute
    num_dogs = 2  # There are 2 dogs barking
    minutes = 10  # The dogs will bark for 10 minutes

    # Calculate the total number of barks
    total_barks = barks_per_minute * num_dogs * minutes
    result = total_barks
    return result

print(solution())