def solution():
    """Sabrina is collecting herbs to make a poultice for her grandmother. She needs twice as many basil leaves as sage leaves and 5 fewer sage leaves than verbena leaves. If she needs 12 basil leaves, how many leaves total does she need?"""
    # Define the number of basil leaves
    basil_leaves = 12

    # Calculate the number of sage leaves
    sage_leaves = basil_leaves // 2

    # Calculate the number of verbena leaves
    verbena_leaves = sage_leaves + 5

    # Calculate the total number of leaves needed
    total_leaves = basil_leaves + sage_leaves + verbena_leaves

    # return the result
    result = total_leaves
    return result

print(solution())