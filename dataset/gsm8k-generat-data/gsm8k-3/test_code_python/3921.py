def solution():
    """Daisy is climbing trees all around her neighborhood and starts to notice the number of branches and the height. The first tree she climbs is 50 feet tall and has 200 branches. The second tree she climbs is 40 feet tall and has 180 branches. The third tree she climbs is 60 feet tall and has 180 branches. The final tree she climbs is 34 feet tall and has 153 branches. On average, how many branches do these trees have per foot?"""
    # Calculate the total number of branches
    total_branches = 200 + 180 + 180 + 153

    # Calculate the total height
    total_height = 50 + 40 + 60 + 34

    # Calculate the average number of branches per foot
    avg_branches_per_foot = total_branches / total_height

    # Display the average number of branches per foot
    result = avg_branches_per_foot
    return result

print(solution())