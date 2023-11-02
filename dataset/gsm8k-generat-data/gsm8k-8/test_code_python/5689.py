def solution():
    # Calculate the number of times one bunny comes out of the burrow in a minute
    bunny_per_minute = 3

    # Calculate the number of times one bunny comes out of the burrow in an hour
    bunny_per_hour = bunny_per_minute * 60

    # Calculate the number of times one bunny comes out of the burrow in 10 hours
    bunny_per_10_hours = bunny_per_hour * 10

    # Calculate the total number of times 20 bunnies will have come out of their burrows in 10 hours
    total_bunny_out = bunny_per_10_hours * 20

    result = total_bunny_out
    return result

print(solution())