def solution():
    bicycles = 3
    tricycles = 4
    unicycles = 7
    bicycle_wheels = 2
    tricycle_wheels = 3
    unicycle_wheels = 1
    total_wheels = (bicycles * bicycle_wheels) + (tricycles * tricycle_wheels) + (unicycles * unicycle_wheels)
    result = total_wheels
    return result

print(solution())