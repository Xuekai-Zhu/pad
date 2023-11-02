def solution():
    """Gerald had 20 toy cars. He donated 1/4 of his toy cars to an orphanage. How many toy cars does Gerald have left?"""
    total_cars = 20
    donated_cars = total_cars / 4
    cars_left = total_cars - donated_cars
    result = cars_left
    return result

print(solution())