def solution():
    """Jill and her brother Jack are going apple picking. Jill's basket can hold twice as much as Jack's basket when both are full. Jack's basket is full when it has 12 apples, but currently space for 4 more. How many times could Jack's current number of apples fit into Jill's basket?"""
    jack_full = 12
    jack_current = jack_full - 4
    jill_full = 2 * jack_full
    jill_current = 2 * jack_current
    times_in_jill = jill_current // jack_current
    result = times_in_jill
    return result

print(solution())