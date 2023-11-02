def solution():
    """Jack is stranded on a desert island. He wants some salt to season his fish. He collects 2 liters of seawater in an old bucket. If the water is 20% salt, how many ml of salt will Jack get when all the water evaporates?"""
    # Define the volume of seawater collected in liters
    seawater_volume = 2

    # Calculate the volume of salt in the seawater in milliliters (ml)
    salt_volume = seawater_volume * 1000 * 0.2

    # return the result
    result = salt_volume
    return result

print(solution())