def solution():
    """Sabrina is collecting herbs to make a poultice for her grandmother. She needs twice as many basil leaves as sage leaves and 5 fewer sage leaves than verbena leaves. If she needs 12 basil leaves, how many leaves total does she need?"""
    # Calculate the number of sage leaves needed
    sage_leaves = 12 / 2
    # Calculate the number of verbena leaves needed
    verbena_leaves = sage_leaves + 5
    # Calculate the total number of leaves needed
    total_leaves = 12 + sage_leaves + verbena_leaves
    result = total_leaves
    return result

print(solution())