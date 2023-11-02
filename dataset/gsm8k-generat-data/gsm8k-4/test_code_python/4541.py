def solution():
    """Mark is baking bread. He has to let it rise for 120 minutes twice. He also needs to spend 10 minutes kneading it and 30 minutes baking it. How many minutes does it take Mark to finish making the bread?"""
    # Calculate the time needed for rising the bread
    rise_time = 120 * 2

    # Calculate the time needed for kneading and baking the bread
    prep_time = 10 + 30

    # Calculate the total time
    total_time = rise_time + prep_time

    # return the result
    result = total_time
    return result

print(solution())