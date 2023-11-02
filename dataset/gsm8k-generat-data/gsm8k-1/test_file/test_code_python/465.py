def solution():
    """Mary has 6 jars of sprinkles in her pantry. Each jar of sprinkles can decorate 8 cupcakes. Mary wants to bake enough cupcakes to use up all of her sprinkles. If each pan holds 12 cupcakes, how many pans worth of cupcakes should she bake?"""
    jars_of_sprinkles = 6
    cupcakes_per_jar = 8
    total_cupcakes = jars_of_sprinkles * cupcakes_per_jar
    cupcakes_per_pan = 12
    pans_needed = total_cupcakes // cupcakes_per_pan
    if total_cupcakes % cupcakes_per_pan != 0:
        pans_needed += 1
    result = pans_needed
    return result

print(solution())