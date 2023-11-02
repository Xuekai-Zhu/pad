def solution():
    """Bill is doing weight training before trying out for the boxing team. He gets two 2-gallon jugs and fills them 70% full with sand. If sand has a density of 5 pounds/gallon, how many pounds do Bill's improvised weights weigh?"""
    jug_size = 2
    fill_percentage = 0.7
    sand_density = 5
    fill_amount = jug_size * fill_percentage
    weight = fill_amount * sand_density * 2
    result = weight
    
    return result

print(solution())