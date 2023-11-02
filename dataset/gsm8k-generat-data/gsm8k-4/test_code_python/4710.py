def solution():
    """The distance between Arizona and New York is around 2,000 miles by plane. The distance between the 2 different US states increases by 40% if someone decides to drive instead of flying. Missouri is midway between Arizona and New York. How far away is Missouri from New York if someone decides to go by car?"""
    # Define the distance between Arizona and New York by plane
    arizona_ny_plane = 2000

    # Calculate the distance between Arizona and New York by car
    arizona_ny_car = arizona_ny_plane * 1.4

    # Calculate the distance between Missouri and New York by car
    mo_ny_car = (arizona_ny_car - arizona_ny_plane) / 2

    # Return the result
    result = mo_ny_car
    return result

print(solution())