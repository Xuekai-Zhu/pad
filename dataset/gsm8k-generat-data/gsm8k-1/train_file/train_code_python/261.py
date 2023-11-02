def solution():
    """Jill and her brother Jack are going apple picking. Jill's basket can hold twice as much as Jack's basket when both are full. Jack's basket is full when it has 12 apples, but currently space for 4 more. How many times could Jack's current number of apples fit into Jill's basket?"""
    jack_basket_full = 12
    jack_basket_current = 8
    jill_basket_full = 2 * jack_basket_full
    jack_capacity = jack_basket_full - jack_basket_current
    jill_capacity = jill_basket_full - jack_basket_full
    times_jack_fits = jill_capacity // jack_capacity
    result = times_jack_fits
    return result

print(solution())