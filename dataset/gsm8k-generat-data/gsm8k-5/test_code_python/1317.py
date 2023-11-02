def solution():
    # Carlos runs around the entire block in 3 minutes
    carlos_time = 3 * 60  # Convert to seconds

    # Diego runs around half the block in 2.5 minutes
    diego_time = 2.5 * 60  # Convert to seconds
    # Since Diego runs half the block in 2.5 minutes, we know that he runs the entire block in 5 minutes
    # But he didn't finish due to being tripped by a dog, so we don't need to consider his time further

    # Calculate the average time for the race
    total_distance = 1  # The racers are just going around the block once
    total_time = carlos_time + diego_time  # Sum of Carlos's and Diego's times
    avg_time = total_time / (total_distance * 2)  # Divide by total distance multiplied by number of racers
    result = avg_time
    return result

print(solution())