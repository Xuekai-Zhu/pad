def solution():
    """A bumper car rink has 12 red cars. They have 2 fewer green cars than they have red cars. They have 3 times the number of blue cars as they have green cars. The rink also has yellow cars. If the rink has 75 cars in total how many yellow cars do they have?"""
    red_cars = 12
    green_cars = red_cars - 2
    blue_cars = 3 * green_cars
    total_cars = 75
    yellow_cars = total_cars - (red_cars + green_cars + blue_cars)
    result = yellow_cars
    return result

print(solution())