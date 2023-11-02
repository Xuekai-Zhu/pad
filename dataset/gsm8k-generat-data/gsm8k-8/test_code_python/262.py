def solution():
    # Define the capacity of Jack's basket
    jack_capacity = 12 + 4

    # Define the capacity of Jill's basket
    jill_capacity = 2 * jack_capacity

    # Calculate the number of times Jack's current apples could fit into Jill's basket
    times_fit = jill_capacity // jack_capacity
    result = times_fit
    return result

print(solution())