def solution():
    
    jack_basket_full = 12
    jack_basket_current = 8
    jill_basket_full = 2 * jack_basket_full
    jack_capacity = jack_basket_full - jack_basket_current
    jill_capacity = jill_basket_full - jack_basket_full
    times_jack_fits = jill_capacity // jack_capacity
    result = times_jack_fits
    return result

print(solution())