def solution():
    """Karen’s work tote bag is twice the weight of her husband Kevin’s briefcase when the briefcase is empty. When Kevin puts his laptop and work papers in his briefcase, it is twice the weight of Karen’s tote. Kevin’s work papers are a sixth of the weight of the contents of his full briefcase. If Karen’s tote weighs 8 pounds, how many more pounds does Kevin’s laptop weigh than Karen’s tote?"""
    # Define Karen's tote weight
    karen_tote = 8

    # Define the weight ratio between Karen's tote and Kevin's briefcase
    tote_to_briefcase_ratio = 2

    # Calculate Kevin's empty briefcase weight
    kevin_briefcase_empty = karen_tote / tote_to_briefcase_ratio

    # Calculate the weight of Kevin's laptop and work papers
    kevin_workpapers_ratio = 1 / 6
    kevin_laptop_weight = kevin_briefcase_empty * kevin_workpapers_ratio
    kevin_workpapers_weight = kevin_briefcase_empty - kevin_laptop_weight
    kevin_briefcase_full = kevin_laptop_weight + kevin_workpapers_weight

    # Calculate how many more pounds Kevin's laptop weighs compared to Karen's tote
    laptop_weight_diff = kevin_laptop_weight - karen_tote

    # Return the result
    result = laptop_weight_diff
    return result

print(solution())