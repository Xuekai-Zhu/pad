def solution():
    # Calculate the total number of wheels on the cars
    wheels_on_cars = 2 * 4  
    
    # Calculate the total number of wheels on the bikes and the trash can
    wheels_on_bikes_trash_can = 2 * 2 + 1 * 2  
    
    # Calculate the total number of wheels on the tricycle and the roller skates
    wheels_on_tricycle_roller_skates = 3 + 2 * 4  
    
    # Calculate the total number of wheels
    total_wheels = wheels_on_cars + wheels_on_bikes_trash_can + wheels_on_tricycle_roller_skates
    result = total_wheels
    return result

print(solution())