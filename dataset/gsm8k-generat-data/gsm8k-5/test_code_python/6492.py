def solution():
    crows = 3
    worms = 30
    time = 1
    crows_new = 5
    time_new = 2

    # Calculate the rate at which the crows eat worms
    rate = worms / (crows * time)

    # Calculate the total number of worms eaten by 5 crows in 2 hours
    worms_new = rate * (crows_new * time_new)

    result = worms_new
    return result

print(solution())