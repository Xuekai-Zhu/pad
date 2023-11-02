def solution():
    trolls_by_path = 6  # Erin counts 6 trolls by the path
    trolls_under_bridge = (6 + 6) / 4  # Erin counts 6 less than 4 times the number of trolls under the bridge
    trolls_in_plains = trolls_under_bridge / 2  # Erin counts half as many trolls in the plains as under the bridge

    # Calculate the total number of trolls Erin counted
    total_trolls = trolls_by_path + trolls_under_bridge + trolls_in_plains
    result = total_trolls
    return result

print(solution())