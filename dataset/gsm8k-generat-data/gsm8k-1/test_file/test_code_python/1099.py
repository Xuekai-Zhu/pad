def solution():
    """A jellyfish tank has numerous jellyfish in it. A fifth of the jellyfish are large, and a third of the large jellyfish change color from green to blue under UV light. The other jellyfish are small and always stay blue. When a UV light turned on, 6 jellyfish changed color. How many jellyfish are in the tank?"""
    total_jellyfish = 0
    large_jellyfish = 0
    green_to_blue_jellyfish = 0
    
    # Find the total number of jellyfish
    for i in range(1,101):
        if i % 5 == 0:
            large_jellyfish += 1
            total_jellyfish += 1
        else:
            total_jellyfish += 1
    
    # Find the number of large jellyfish that change color
    green_to_blue_jellyfish = large_jellyfish // 3
    
    # Find the total number of jellyfish that changed color
    total_color_change = 6
    
    # Find the total number of blue jellyfish
    blue_jellyfish = total_jellyfish - green_to_blue_jellyfish - large_jellyfish
    
    # Find the number of large jellyfish that stayed green
    green_jellyfish = large_jellyfish - green_to_blue_jellyfish
    
    # Find the number of small jellyfish
    small_jellyfish = blue_jellyfish - green_jellyfish
    
    result = total_jellyfish
    return result

print(solution())