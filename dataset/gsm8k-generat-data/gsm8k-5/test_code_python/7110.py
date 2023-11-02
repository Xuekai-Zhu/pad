def solution():
    tank_capacity = 600  # The tank can hold 600 gallons of water
    bucket_capacity = 5  # Each bucket can hold 5 gallons of water
    jack_capacity = 2 * bucket_capacity  # Jack can carry 2 buckets of water at a time
    jill_capacity = bucket_capacity  # Jill can carry 1 bucket of water at a time

    # Let's assume that Jack makes 3 trips to the well and back, and Jill makes 2 trips
    jack_time = 3
    jill_time = 2

    # Calculate the total capacity delivered by Jack and Jill in their combined trips
    total_capacity = (jack_time * jack_capacity) + (jill_time * jill_capacity)

    # Calculate the number of trips Jill needs to make to deliver the remaining water
    remaining_capacity = tank_capacity - total_capacity
    jill_trips = remaining_capacity / jill_capacity

    result = jill_trips
    return result

print(solution())