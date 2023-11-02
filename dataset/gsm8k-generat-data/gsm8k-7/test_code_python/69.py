def solution():
    num_starfish = 7
    arms_per_starfish = 5

    num_seastar = 1
    arms_per_seastar = 14

    # Calculate the total number of arms of all starfish
    total_starfish_arms = num_starfish * arms_per_starfish

    # Calculate the total number of arms of the seastar
    total_seastar_arms = num_seastar * arms_per_seastar

    # Calculate the total number of arms of all animals collected
    total_arms = total_starfish_arms + total_seastar_arms
    result = total_arms
    return result

print(solution())