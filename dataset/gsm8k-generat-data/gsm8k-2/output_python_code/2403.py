def solution():
    """Tommy has 3 toy cars. His neighbor, Jessie, has 3 cars too. Jessie's older brother has 5 more cars than Tommy and Jessie. How many cars do the three of them have altogether?"""
    tommy_cars = 3
    jessie_cars = 3
    older_brother_cars = tommy_cars + jessie_cars + 5
    total_cars = tommy_cars + jessie_cars + older_brother_cars
    result = total_cars
    return result

print(solution())