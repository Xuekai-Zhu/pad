def solution():
    item_needed_for_surgery = "scalpel"
    domain_of_ontology = "philosophical"
    if item_needed_for_surgery not in domain_of_ontology:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())