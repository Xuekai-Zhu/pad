def solution():
    bach_influence = True
    metallica_collaborated_with_symphony = True
    deep_purple_cited_classical_influences = True
    if bach_influence and (metallica_collaborated_with_symphony or deep_purple_cited_classical_influences):
        result = "yes"
    else:
        result = "no"
    return result

print(solution())