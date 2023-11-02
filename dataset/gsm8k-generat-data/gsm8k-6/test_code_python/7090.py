def solution():
    # Set up equations
    s + st + 4st = 1100  # the total number of berries is 1100
    st = 2sy  # Steve has double the berries of Skylar
    s = 4st  # Stacy has four times as many berries as Steve

    # Simplify and solve for Stacy's berries
    s + 3st = 1100  # substitute 4st into the first equation
    s + 3(2sy) = 1100  # substitute 2sy into the above equation
    s + 6sy = 1100
    s(1 + 6s) = 1100
    7s = 1100
    s = 157.14...  # round to the nearest whole number
    st = 2sy = 2*78.57... = 157.14...
    berries_Stacy = 4st = 4*157.14... = 628.57... ≈ 629

    result = berries_Stacy
    return result

print(solution())