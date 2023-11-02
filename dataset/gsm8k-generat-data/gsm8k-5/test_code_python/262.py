def solution():
    jack_basket_capacity = 12  # Jack's basket can hold 12 apples when it's full
    jack_current_apples = jack_basket_capacity - 4  # Jack's basket currently has space for 4 more apples
    jill_basket_capacity = jack_basket_capacity * 2  # Jill's basket can hold twice as much as Jack's basket

    # Calculate how many times Jack's current number of apples can fit into Jill's basket
    times_jack_apples_fit_in_jill_basket = jill_basket_capacity // jack_current_apples
    result = times_jack_apples_fit_in_jill_basket
    return result

print(solution())