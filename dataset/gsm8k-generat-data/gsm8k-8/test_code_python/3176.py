def solution():
    # Define variables for the three children's ages
    cynthia = 0
    rebecca = 0
    freddy = 0

    # Use the fact that the three ages add up to 35 to solve for Cynthia's age
    cynthia = 35 - (rebecca + freddy)

    # Use the information about Matthew's age to solve for Rebecca's age
    rebecca = (freddy - 4) - 2

    # Use the fact that the three ages add up to 35 again to solve for Freddy's age
    freddy = 35 - (cynthia + rebecca)

    # Return Freddy's age as the final result
    result = freddy
    return result

print(solution())