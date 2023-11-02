def solution():
    """For homework, Juan's teacher asked everyone in the class, to write down the different types of transportation (cars, trucks, bicycles, skateboards etc) they saw on their way home that afternoon. After school, Juan walked home and saw the following: 15 cars, 3 bicycles, 8 pickup trucks and 1 tricycle. How many tires in total were there on the vehicles Juan saw?"""
    cars = 15
    bicycles = 3
    trucks = 8
    tricycles = 1
    tires_per_car = 4
    tires_per_truck = 4
    tires_per_bicycle = 2
    tires_per_tricycle = 3
    total_tires = (cars * tires_per_car) + (trucks * tires_per_truck) + (bicycles * tires_per_bicycle) + (tricycles * tires_per_tricycle)
    result = total_tires
    return result

print(solution())