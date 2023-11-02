def solution():
    first_car = "Model T"
    first_car_year = 1908
    mini_year = 1959
    
    if mini_year > first_car_year and first_car != "Mini":
        result = "no"
    else:
        result = "yes"
        
    return result

print(solution())