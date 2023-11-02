def solution():
    drew_age = 12
    years_in_future = 5

    # Calculate Drew's age in the future
    drew_future_age = drew_age + years_in_future

    # Calculate Sam's age in the future (when Sam is 3 times as old as Drew)
    sam_future_age = 3 * drew_future_age

    # Calculate Sam's current age
    sam_age = sam_future_age - years_in_future
    result = sam_age
    return result

print(solution())