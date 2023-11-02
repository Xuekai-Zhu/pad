def solution():
    black_salt_contains_sulfur = True
    sulfur_smells_like_rotten_eggs = True
    if black_salt_contains_sulfur and sulfur_smells_like_rotten_eggs:
        result = "yes, food made with black salt would smell of sulfur."
    else:
        result = "no, food made with black salt would not necessarily smell of sulfur."
    return result

print(solution())