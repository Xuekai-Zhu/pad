def solution():
    rides_rollercoaster = 3
    rides_catapult = 2
    rides_ferris_wheel = 1
    cost_rollercoaster = 4
    cost_catapult = 4
    cost_ferris_wheel = 1
    total_cost = (rides_rollercoaster * cost_rollercoaster) + (rides_catapult * cost_catapult) + (rides_ferris_wheel * cost_ferris_wheel)
    result = total_cost
    return result

print(solution())