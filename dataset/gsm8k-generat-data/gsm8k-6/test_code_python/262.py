def solution():
    # Calculate the capacity of Jill's basket
    jill_capacity = 2 * 12  # Jill's basket can hold twice as much as Jack's basket when both are full

    # Calculate the number of apples in Jack's basket
    jack_apples = 12 - 4  # Jack's basket is full when it has 12 apples, but currently space for 4 more

    # Calculate the number of times Jack's current number of apples could fit into Jill's basket
    times_jack_fits = jill_capacity // jack_apples
    result = times_jack_fits
    return result

print(solution())