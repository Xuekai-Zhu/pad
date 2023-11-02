def solution():
    """A factory manufactures cars with 5 doors. The factory was planning to produce 200 cars but due to metal shortages, they decreased the production by 50 cars. Due to a pandemic, they also had to cut production by another 50%. How many doors will the factory produce?"""
    car_doors = 5
    planned_cars = 200
    metal_shortage_cars = planned_cars - 50
    pandemic_cars = metal_shortage_cars * 0.5
    total_cars = metal_shortage_cars - pandemic_cars
    total_doors = total_cars * car_doors
    result = total_doors
    return result

print(solution())