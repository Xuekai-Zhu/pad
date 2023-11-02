def solution():
    """Jill and her brother Jack are going apple picking.  Jill's basket can hold twice as much as Jack's basket when both are full.  Jack's basket is full when it has 12 apples, but currently space for 4 more.  How many times could Jack's current number of apples fit into Jill's basket?"""
    # Define the number of apples in Jack's basket
    jack_apples = 12 - 4

    # Define Jill's basket size in terms of Jack's basket size
    jill_basket_size = 2

    # Calculate the number of times Jack's current number of apples could fit into Jill's basket
    times_into_jill = jill_basket_size * (jack_apples / jill_basket_size)

    result = times_into_jill
    return result

print(solution())