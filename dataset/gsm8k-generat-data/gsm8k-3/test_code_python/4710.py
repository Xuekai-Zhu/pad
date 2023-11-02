def solution():
    """The distance between Arizona and New York is around 2,000 miles by plane.
    The distance between the 2 different US states increases by 40% if someone decides to drive instead of flying.
    Missouri is midway between Arizona and New York. How far away is Missouri from New York if someone decides to go by car?"""
    # Define the distance between Arizona and New York by plane
    plane_distance = 2000

    # Calculate the distance between Arizona and Missouri by plane
    arizona_missouri_plane = plane_distance / 2

    # Calculate the distance between Missouri and New York by plane
    missouri_newyork_plane = plane_distance / 2

    # Calculate the distance between Arizona and Missouri by car
    arizona_missouri_car = arizona_missouri_plane * 1.4

    # Calculate the distance between Missouri and New York by car
    missouri_newyork_car = missouri_newyork_plane * 1.4

    # Calculate the total distance between Missouri and New York by car
    total_distance = arizona_missouri_car + missouri_newyork_car

    # Display the total distance
    result = total_distance
    return result

print(solution())