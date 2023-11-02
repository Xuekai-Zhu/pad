def solution():
    """Rani has ten more crabs than Monic, who has 4 fewer crabs than Bo. If Bo has 40 crabs, calculate the total number of crabs the three have together."""
    bo_crabs = 40
    monic_crabs = bo_crabs - 4
    rani_crabs = monic_crabs + 10
    total_crabs = bo_crabs + monic_crabs + rani_crabs
    result = total_crabs
    return result

print(solution())