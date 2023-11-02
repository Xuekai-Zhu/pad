def solution():
    # Calculate the total volume of the iron bars
    total_volume = 12 * 8 * 6 * 10  # volume = length x width x height x number of bars
    
    # Calculate the number of iron balls that can be formed
    num_balls = total_volume // 8  # // operator performs integer division
    
    result = num_balls
    return result

print(solution())