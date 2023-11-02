def solution():
    """Karen’s work tote bag is twice the weight of her husband Kevin’s briefcase when the briefcase is empty. When Kevin puts his laptop and work papers in his briefcase, it is twice the weight of Karen’s tote. Kevin’s work papers are a sixth of the weight of the contents of his full briefcase. If Karen’s tote weighs 8 pounds, how many more pounds does Kevin’s laptop weigh than Karen’s tote?"""

    # Let x be the weight of Kevin's empty briefcase
    x = 1

    # Karen's tote weighs 8 pounds
    karen_weight = 8

    # Kevin's briefcase is twice as heavy as Karen's tote when empty
    kevin_weight = x * 2

    # When Kevin adds his laptop and work papers, his briefcase is twice as heavy as Karen's tote
    kevin_contents = kevin_weight * 2  # total weight of Kevin's briefcase with contents

    # Kevin's work papers are a sixth of the weight of the contents of his full briefcase
    kevin_work_papers = kevin_contents / 6

    # Kevin's briefcase with contents and work papers
    kevin_full = kevin_contents + kevin_work_papers

    # Karen's tote weighs 8 pounds
    karen_weight = 8

    # Kevin's laptop weighs the difference between his full briefcase and Karen's tote
    kevin_laptop_weight = kevin_full - karen_weight

    # Display the weight of Kevin's laptop compared to Karen's tote
    result = kevin_laptop_weight - karen_weight
    return result

print(solution())