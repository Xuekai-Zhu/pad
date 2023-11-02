def solution():
    total_cupcakes = 144  # Mary wants 144 cupcakes
    cherry_cupcakes = 36
    berry_cupcakes = 48
    
    # Calculate how many cupcakes Mary has made
    cupcakes_made = cherry_cupcakes + berry_cupcakes

    # Calculate how many cupcakes Mary still needs to make
    cupcakes_left = total_cupcakes - cupcakes_made

    # Make an even number of chocolate and vanilla cupcakes
    even_cupcakes = cupcakes_left - (cupcakes_left % 2)

    # Divide the even cupcakes into chocolate and vanilla
    chocolate_cupcakes = even_cupcakes / 2
    vanilla_cupcakes = even_cupcakes / 2

    result = (chocolate_cupcakes, vanilla_cupcakes)
    return result

print(solution())