def solution():
    # Calculate the distance each person ran per hour
    jim_distance = 16 / 2  # Jim ran 16 miles in 2 hours
    frank_distance = 20 / 2  # Frank ran 20 miles in 2 hours

    # Calculate how many more miles Frank ran than Jim in an hour
    differential = frank_distance - jim_distance
    result = differential
    return result

print(solution())