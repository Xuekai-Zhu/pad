def solution():
    """Coleen loved sprinkles. At the beginning of the day, she had twelve cans of sprinkles. After applying sprinkles to her hair, her clothing and her pets, she had 3 less than half as many cans of sprinkles as she started out with. How many cans of sprinkles remained?"""
    # Define the initial number of cans of sprinkles
    initial_cans = 12

    # Calculate the number of cans she used
    used_cans = (initial_cans / 2) - 3

    # Calculate the number of cans remained
    remained_cans = initial_cans - used_cans

    # return the result
    result = remained_cans
    return result

print(solution())