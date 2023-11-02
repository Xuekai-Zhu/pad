def solution():
    
    num_bicycles = 3
    num_tricycles = 4
    num_unicycles = 7

    wheels_per_bicycle = 2
    wheels_per_tricycle = 3
    wheels_per_unicycle = 1

    total_wheels = (num_bicycles * wheels_per_bicycle) + (num_tricycles * wheels_per_tricycle) + (num_unicycles * wheels_per_unicycle)
    result = total_wheels
    return result

print(solution())