def solution():
    """Jill and her brother Jack are going apple picking. Jill's basket can hold twice as much as Jack's basket when both are full. Jack's basket is full when it has 12 apples, but currently space for 4 more. How many times could Jack's current number of apples fit into Jill's basket?"""
    # Define the size of Jack's basket
    jack_basket_size = 12

    # Define the current number of apples in Jack's basket
    jack_apple_count = jack_basket_size - 4

    # Define the size of Jill's basket
    jill_basket_size = jack_basket_size * 2

    # Calculate how many times Jack's current number of apples could fit into Jill's basket
    jill_apple_count = jill_basket_size // 2
    jack_fit_count = jack_apple_count // jill_apple_count

    result = jack_fit_count
    return result

print(solution())