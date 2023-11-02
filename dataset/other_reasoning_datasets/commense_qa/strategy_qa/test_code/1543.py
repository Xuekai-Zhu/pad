def solution():
    requires_human_intelligence = True
    is_amoeba_single_celled_organism = True
    if requires_human_intelligence and not is_amoeba_single_celled_organism:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())