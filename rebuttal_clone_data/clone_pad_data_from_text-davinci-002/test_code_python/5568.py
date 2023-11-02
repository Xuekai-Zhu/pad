def solution():
    total_cupcakes = 144
    cherry_cupcakes = 36
    berry_cupcakes = 48
    chocolate_cupcakes = (total_cupcakes - cherry_cupcakes - berry_cupcakes) / 2
    vanilla_cupcakes = (total_cupcakes - cherry_cupcakes - berry_cupcakes) / 2
    result = "Mary should make {} chocolate cupcakes and {} vanilla cupcakes.".format(chocolate_cupcakes, vanilla_cupcakes)
    return result

print(solution())