def solution():
    """A factory manufactures cars with 5 doors. The factory was planning to produce 200 cars but due to metal shortages, they decreased the production by 50 cars. Due to a pandemic, they also had to cut production by another 50%. How many doors will the factory produce?"""
    cars_planned = 200
    cars_shortage = 50
    final_cars = (cars_planned - cars_shortage) * 0.5
    doors_per_car = 5
    total_doors = final_cars * doors_per_car
    result = total_doors
    return result

print(solution())