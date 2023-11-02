def solution():
    """Stan weighs 5 more pounds than Steve. Steve is eight pounds lighter than Jim. If Jim weighs 110 pounds and the three of them crowd onto a scale at the same time, what is their total weight?"""
    jim_weight = 110
    steve_weight = jim_weight - 8
    stan_weight = steve_weight + 5
    total_weight = jim_weight + steve_weight + stan_weight
    result = total_weight
    return result

print(solution())