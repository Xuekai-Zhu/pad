def solution():
    """Paul needs 63 cupcakes for a birthday party happening on Saturday. He already has 8 chocolate cupcakes and 40 toffee cupcakes. How many more cupcakes should Paul buy?"""
    total_cupcakes = 63
    chocolate_cupcakes = 8
    toffee_cupcakes = 40
    cupcakes_needed = total_cupcakes - (chocolate_cupcakes + toffee_cupcakes)
    result = cupcakes_needed
    return result

print(solution())