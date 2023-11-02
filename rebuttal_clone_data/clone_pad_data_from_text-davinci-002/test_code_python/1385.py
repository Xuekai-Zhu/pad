def solution():
    Cole_backyard_side1 = 9
    Cole_backyard_side2 = 18
    Cole_side_of_fence = Cole_backyard_side1 + Cole_backyard_side2
    neighbor_contribution1 = Cole_side_of_fence / 2
    neighbor_contribution2 = Cole_side_of_fence / 3
    Cole_fence_cost = Cole_side_of_fence * 3
    Cole_cost = Cole_fence_cost - neighbor_contribution1 - neighbor_contribution2
    
    result = Cole_cost
    
    return result

print(solution())