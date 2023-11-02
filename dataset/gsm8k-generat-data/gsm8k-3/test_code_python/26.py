def solution():
    """Jack is stranded on a desert island. He wants some salt to season his fish. He collects 2 liters of seawater in an old bucket. If the water is 20% salt, how many ml of salt will Jack get when all the water evaporates?"""
    # Define the volume of seawater collected and the concentration of salt
    seawater_volume = 2  # liters
    salt_concentration = 0.2  # 20%

    # Calculate the total amount of salt in the seawater
    total_salt = seawater_volume * salt_concentration  # liters

    # Convert the total amount of salt to milliliters
    total_salt_ml = total_salt * 1000  # milliliters

    # Return the result
    result = total_salt_ml
    return result

print(solution())