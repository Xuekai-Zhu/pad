def solution():
    """Karen’s work tote bag is twice the weight of her husband Kevin’s briefcase when the briefcase is empty.
    When Kevin puts his laptop and work papers in his briefcase,
    it is twice the weight of Karen’s tote.
    Kevin’s work papers are a sixth of the weight of the contents of his full briefcase.
    If Karen’s tote weighs 8 pounds,
    how many more pounds does Kevin’s laptop weigh than Karen’s tote?"""
    karen_tote_weight = 8
    kevin_briefcase_empty_weight = karen_tote_weight / 2
    kevin_briefcase_total_weight = 4 * karen_tote_weight
    kevin_briefcase_laptop_weight = kevin_briefcase_total_weight - kevin_briefcase_empty_weight - (kevin_briefcase_total_weight / 6)
    weight_difference = kevin_briefcase_laptop_weight - karen_tote_weight
    result = weight_difference
    return result

print(solution())