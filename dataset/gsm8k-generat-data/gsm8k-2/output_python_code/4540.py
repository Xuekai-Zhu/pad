def solution():
    """Mark is baking bread. He has to let it rise for 120 minutes twice. He also needs to spend 10 minutes kneading it and 30 minutes baking it. How many minutes does it take Mark to finish making the bread?"""
    rise_time = 120
    knead_time = 10
    bake_time = 30
    total_time = (rise_time * 2) + knead_time + bake_time
    result = total_time
    return result

print(solution())