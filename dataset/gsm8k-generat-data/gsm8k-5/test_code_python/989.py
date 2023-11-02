def solution():
    caleb_capacity = 7  # Caleb's bucket can hold 7 gallons
    cynthia_capacity = 8  # Cynthia's bucket can hold 8 gallons
    pool_capacity = 105  # The pool can hold 105 gallons of water

    total_capacity = caleb_capacity + cynthia_capacity  # The total capacity of both buckets combined
    total_trips = pool_capacity / total_capacity  # The total number of trips required to fill the pool

    # Round up the number of trips to a whole number
    trips = math.ceil(total_trips)

    result = trips
    return result

print(solution())