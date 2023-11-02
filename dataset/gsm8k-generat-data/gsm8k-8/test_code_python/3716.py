def solution():
    start_elevation = 400
    rate = 10
    time = 5

    new_elevation = start_elevation - (rate * time)
    result = new_elevation
    return result

print(solution())