def solution():
    # Calculate the total amount of sand collected by Eden, Mary and Iris
    eden_sand = 4  
    mary_sand = eden_sand + 3  
    iris_sand = mary_sand - 1  
    total_sand = (eden_sand + mary_sand + iris_sand) * 2  # each bucket contains 2 pounds of sand
    result = total_sand
    return result

print(solution())