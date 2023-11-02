def solution():
    """Carlos and Diego are racing around the block. Carlos runs around the entire block in 3 minutes. Diego runs around half the block in 2.5 minutes and then is tripped by a dog and can't finish. Assuming he kept up the same speed the entire race, what would've been the average time in seconds for the racers?"""
    # Define the time and distance for Carlos
    carlos_time = 3
    carlos_distance = 1

    # Define the time and distance for Diego
    diego_time = 2.5
    diego_distance = 0.5

    # Calculate the speed of Diego
    diego_speed = diego_distance / (diego_time / 60)

    # Calculate the remaining distance for Diego
    remaining_distance = carlos_distance - diego_distance 

    # Calculate the time it would take for Diego to complete the race
    remaining_time = (remaining_distance / (diego_speed / 60))

    # Calculate the average time for the racers
    total_time = carlos_time + remaining_time
    average_time = (total_time / 2) * 60

    # return the result in seconds
    result = average_time
    return result

print(solution())