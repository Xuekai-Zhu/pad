def solution():
    """Marcus is making calzones. It takes him 20 minutes to saute the onions and a quarter of that time to saute the garlic and peppers. It takes him 30 minutes to knead the dough, twice as long to let it rest, and 1/10th the combined kneading and resting time to assemble the calzones. How many minutes does Marcus spend on the calzones total?"""
    # Calculate the time to saute the garlic and peppers
    saute_time = 20 / 4
    garlic_pepper_time = saute_time

    # Calculate the time to let the dough rest
    rest_time = 30 * 2

    # Calculate the combined kneading and resting time
    knead_rest_time = 30 + rest_time

    # Calculate the time to assemble the calzones
    assemble_time = knead_rest_time / 10

    # Calculate the total time spent on the calzones
    total_time = 20 + garlic_pepper_time + knead_rest_time + assemble_time

    # Display the total time
    result = total_time
    return result

print(solution())