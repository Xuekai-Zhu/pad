def solution():
    total_donuts = 50
    donuts_eaten = 2
    donuts_taken = 4
    donuts_stolen = (total_donuts - donuts_eaten - donuts_taken) / 2
    donuts_left = total_donuts - donuts_eaten - donuts_taken - donuts_stolen
    result = donuts_left
    return result

print(solution())