def solution():
    """Jill and her brother Jack are going apple picking. Jill's basket can hold twice as much as Jack's basket when both are full. Jack's basket is full when it has 12 apples, but currently space for 4 more. How many times could Jack's current number of apples fit into Jill's basket?"""
    jack_capacity = 12
    jack_apples = 12 - 4
    jill_capacity = jack_capacity * 2
    result = jill_capacity / jack_apples
    return result

print(solution())