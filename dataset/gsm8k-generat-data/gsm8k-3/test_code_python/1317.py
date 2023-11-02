def solution():
    """Carlos and Diego are racing around the block. Carlos runs around the entire block in 3 minutes. Diego runs around half the block in 2.5
    minutes and then is tripped by a dog and can't finish. Assuming he kept up the same speed the entire race, what would've been the average time in seconds for the racers?"""
    # Calculate Carlos's time in seconds
    carlos_time = 3 * 60

    # Calculate Diego's speed for the first half of the block
    diego_speed = 0.5 / (2.5 * 60)

    # Calculate the time it would take for Diego to run the entire block at this speed
    diego_time = (1 / diego_speed) / 60

    # Calculate the average time in seconds for the racers
    average_time = (carlos_time + diego_time) / 2

    # Convert the average time to seconds
    average_time_seconds = average_time * 60

    # Display the average time in seconds for the racers
    result = average_time_seconds
    return result

print(solution())