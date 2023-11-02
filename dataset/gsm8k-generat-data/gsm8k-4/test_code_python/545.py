def solution():
    """There are 18 green leaves on each of the 3 tea leaf plants. One-third of them turn yellow and fall off on each of the tea leaf plants. How many green leaves are left on the tea leaf plants?"""
    # Define the initial number of green leaves on each plant
    initial_leaves = 18

    # Calculate the number of leaves that turn yellow and fall off on each plant
    yellow_leaves = initial_leaves / 3

    # Calculate the number of green leaves left on each plant
    green_leaves = initial_leaves - yellow_leaves

    # Calculate the total number of green leaves on all 3 plants
    total_green_leaves = green_leaves * 3

    result = total_green_leaves
    return result

print(solution())