def solution():
    """Gerald had 20 toy cars. He donated 1/4 of his toy cars to an orphanage. How many toy cars does Gerald have left?"""
    initial_cars = 20
    donated_cars = initial_cars / 4
    remaining_cars = initial_cars - donated_cars
    result = remaining_cars
    return result

print(solution())