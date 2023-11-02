def solution():
    num_bicycles = 20
    num_cars = 10
    num_motorcycles = 5

    # Calculate the total number of wheels
    total_wheels = (num_bicycles * 2) + (num_cars * 4) + (num_motorcycles * 2)

    result = total_wheels
    return result

print(solution())