def solution():
    """Mary wants 144 cupcakes for her party. Mary has already made 36 cherry cupcakes, and 48 berry cupcakes. Mary wants to make an even number of chocolate and vanilla cupcakes for the rest. How much of each should she make?"""
    total_cupcakes = 144
    cherry_cupcakes = 36
    berry_cupcakes = 48
    remaining_cupcakes = total_cupcakes - cherry_cupcakes - berry_cupcakes
    chocolate_cupcakes = remaining_cupcakes // 2
    vanilla_cupcakes = remaining_cupcakes // 2
    result = (chocolate_cupcakes, vanilla_cupcakes)
    return result

print(solution())