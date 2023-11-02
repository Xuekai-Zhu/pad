def solution():
    jack_basket_full = 12
    jack_space = 4
    jill_basket_full = 2 * jack_basket_full

    # Calculate Jack's current number of apples
    jack_apples = jack_basket_full - jack_space

    # Calculate the capacity of Jill's basket
    jill_capacity = jill_basket_full - jack_basket_full

    # Calculate how many times Jack's current number of apples could fit into Jill's basket
    times_jacks_apples_fit = jill_capacity / jack_apples
    result = times_jacks_apples_fit
    return result

print(solution())