def solution():
    """Diego baked 12 cakes for his sister's birthday. Donald also baked 4 cakes, but ate 1 while waiting for the party to start. How many cakes are left?"""
    # Define the number of cakes baked by Diego and Donald
    diego_cakes = 12
    donald_cakes = 4

    # Donald ate one cake, so subtract it from his total
    donald_cakes -= 1

    # Calculate the total number of cakes left
    total_cakes = diego_cakes + donald_cakes

    # Display the number of cakes left
    result = total_cakes
    return result

print(solution())