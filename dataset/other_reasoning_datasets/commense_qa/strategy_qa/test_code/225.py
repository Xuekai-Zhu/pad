def solution():
    # Define what sea otters prey on
    sea_otter_prey = ["marine invertebrates", "other aquatic creatures"]
    # Check if spiders are included in their prey
    if "spiders" in sea_otter_prey:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())