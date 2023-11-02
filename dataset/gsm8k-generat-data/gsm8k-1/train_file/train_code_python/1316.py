def solution():
    """Carlos and Diego are racing around the block. Carlos runs around the entire block in 3 minutes. Diego runs around half the block in 2.5 minutes and then is tripped by a dog and can't finish. Assuming he kept up the same speed the entire race, what would've been the average time in seconds for the racers?"""
    carlos_time = 3 * 60  # convert to seconds
    diego_distance = 0.5
    diego_speed = diego_distance / (2.5 * 60)  # convert to minutes
    diego_time = diego_distance / diego_speed
    total_distance = 1  # full block
    total_time = carlos_time + diego_time
    average_time = total_time / 2  # two racers
    result = average_time
    return result

print(solution())