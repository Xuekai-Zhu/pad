def solution():
    """Sabrina is collecting herbs to make a poultice for her grandmother. She needs twice as many basil leaves as sage leaves and 5 fewer sage leaves than verbena leaves. If she needs 12 basil leaves, how many leaves total does she need?"""
    basil_leaves = 12
    sage_leaves = basil_leaves / 2
    verbena_leaves = sage_leaves + 5
    total_leaves = basil_leaves + sage_leaves + verbena_leaves
    result = total_leaves
    return result

print(solution())