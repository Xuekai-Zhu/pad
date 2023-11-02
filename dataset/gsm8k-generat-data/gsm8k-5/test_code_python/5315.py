def solution():
    total_distance = 18  # Sam went a total of 18 miles that day

    # Let's assume the distance of Sam's morning run was x
    # Then the distance Sam walked while grocery shopping was 2x
    # Therefore, the total distance walked and run was x + 2x = 3x
    # And we know that Sam also biked for 12 miles
    # So, the total distance covered by Sam's run, walk, and bike was 3x + 12 = 18

    # Solving for x gives us:
    x = (total_distance - 12) / 3
    result = x
    return result

print(solution())