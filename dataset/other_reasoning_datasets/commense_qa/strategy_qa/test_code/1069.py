def solution():
    # Define the list of four-legged mammals that can swim
    animals_that_can_swim = ["giraffes", "apes"]
    # Check if a snow leopard has four legs and is not a giraffe or ape
    if "snow leopard" not in animals_that_can_swim:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())