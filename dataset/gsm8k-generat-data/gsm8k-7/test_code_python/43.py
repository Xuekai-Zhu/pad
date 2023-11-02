def solution():
    first_eq = 4
    eq_factor = 2
    num_eq = 3

    # Calculate the total number of buildings that collapsed after all earthquakes
    total_buildings = first_eq
    for i in range(num_eq):
        total_buildings += first_eq * (eq_factor ** (i+1))

    result = total_buildings
    return result

print(solution())