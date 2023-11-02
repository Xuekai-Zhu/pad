def solution():
    total_distance = 0  # total distance Nina travels

    for i in range(1, 25):  # Nina travels for 24 months (2 years)
        if i % 2 == 0:  # every second month, Nina travels twice the distance
            total_distance += 800  
        else:
            total_distance += 400

    result = total_distance
    return result

print(solution())