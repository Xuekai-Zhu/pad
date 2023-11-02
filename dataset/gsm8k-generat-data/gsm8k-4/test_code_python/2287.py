def solution():
    """Jason is counting the number of cars that drive by his window. He counted four times as many green cars as red cars, and 6 more red cars than purple cars. If he counted 312 cars total, how many of them were purple?"""
    # Let x be the number of purple cars
    # Then the number of red cars is x+6 and the number of green cars is 4(x+6)
    # The total number of cars is x + x+6 + 4(x+6) = 312
    # Simplifying the equation gives 6x + 30 = 312
    # Solving for x gives x = 47

    # Therefore, there are 47 purple cars
    result = 47
    return result

print(solution())