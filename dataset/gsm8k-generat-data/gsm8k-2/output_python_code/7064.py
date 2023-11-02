def solution():
    """For homework, Juan's teacher asked everyone in the class, to write down the different types of transportation (cars, trucks, bicycles, skateboards etc) they saw on their way home that afternoon. After school, Juan walked home and saw the following: 15 cars, 3 bicycles, 8 pickup trucks and 1 tricycle. How many tires in total were there on the vehicles Juan saw?"""
    cars = 15
    bicycles = 3
    trucks = 8
    tricycles = 1
    car_tires = cars * 4
    bicycle_tires = bicycles * 2
    truck_tires = trucks * 6
    tricycle_tires = tricycles * 3
    total_tires = car_tires + bicycle_tires + truck_tires + tricycle_tires
    result = total_tires
    return result

print(solution())