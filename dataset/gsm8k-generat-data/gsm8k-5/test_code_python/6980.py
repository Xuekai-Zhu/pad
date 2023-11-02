def solution():
    start_donuts = 50  # The box starts with 50 donuts
    eaten_on_ride = 2  # Bill eats 2 donuts on the ride in
    secretary_takes = 4  # The secretary takes 4 donuts when Bill isn't looking
    remaining_donuts = start_donuts - eaten_on_ride - secretary_takes  # The remaining donuts after Bill's commute

    remaining_donuts /= 2  # Half of the remaining donuts are eaten by Bill's coworkers

    result = remaining_donuts
    return result

print(solution())