def solution():
    # Define variables for surrogacy and adoption
    surrogates_available = True
    children_available_for_adoption = True
    # Check if those incapable of reproduction can still be parents
    if surrogates_available or children_available_for_adoption:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())