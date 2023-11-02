def solution():
     square_feet_mowed = 3 * (20 * 15)
     cost_per_square_foot = 0.10
     total_cost = 150
     remaining_cost = total_cost - (square_feet_mowed * cost_per_square_foot)
     square_feet_remaining = remaining_cost / cost_per_square_foot
     result = square_feet_remaining
     return result

print(solution())