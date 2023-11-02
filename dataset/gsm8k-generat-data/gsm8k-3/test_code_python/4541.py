def solution():
    """Mark is baking bread. He has to let it rise for 120 minutes twice. He also needs to spend 10 minutes kneading it and 30 minutes baking it. How many minutes does it take Mark to finish making the bread?"""
    # Calculate the total rising time
    rise_time = 120 * 2

    # Calculate the total time for kneading and baking
    prep_time = 10 + 30

    # Calculate the total time to finish making the bread
    total_time = rise_time + prep_time

    # Display the total time
    result = total_time
    return result

print(solution())