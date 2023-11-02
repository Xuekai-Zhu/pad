def solution():
    sailboat_cost = 60
    ski_boat_cost = 80
    total_cost_sailboat = sailboat_cost + (3 * 2 * ski_boat_cost)
    total_cost_ski_boat = (3 * 2 * sailboat_cost) + ski_boat_cost
    difference = total_cost_ski_boat - total_cost_sailboat
    result = difference
    return result

print(solution())