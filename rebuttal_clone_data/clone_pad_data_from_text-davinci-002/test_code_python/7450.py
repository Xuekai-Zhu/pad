def solution():
    total_campers = 96
    boy_campers = total_campers * 2/3
    girl_campers = total_campers - boy_campers
    marshmallows_needed = boy_campers * 1/2 + girl_campers * 3/4
    result = marshmallows_needed
    return result

print(solution())