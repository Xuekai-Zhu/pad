def solution():
    """Karen’s work tote bag is twice the weight of her husband Kevin’s briefcase when the briefcase is empty. When Kevin puts his laptop and work papers in his briefcase, it is twice the weight of Karen’s tote. Kevin’s work papers are a sixth of the weight of the contents of his full briefcase. If Karen’s tote weighs 8 pounds, how many more pounds does Kevin’s laptop weigh than Karen’s tote?"""
    tote_weight = 8
    briefcase_weight = tote_weight / 2
    briefcase_with_stuff_weight = tote_weight * 2
    laptop_and_papers_weight = briefcase_with_stuff_weight - briefcase_weight
    laptop_weight = laptop_and_papers_weight * (1 - (1/6))
    weight_difference = laptop_weight - tote_weight
    result = weight_difference
    return result

print(solution())