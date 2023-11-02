def solution():
    """A local school is holding a food drive. Mark brings in 4 times as many cans as Jaydon. Jaydon brings in 5 more than twice the amount of cans that Rachel brought in. If there are 135 cans total, how many cans did Mark bring in?"""
    # Define the variables
    rachel_cans = None
    jaydon_cans = None
    mark_cans = None

    total_cans = 135

    # Calculate the number of cans Rachel brought in
    rachel_cans = (total_cans - 5) / 2

    # Calculate the number of cans Jaydon brought in
    jaydon_cans = rachel_cans + 5

    # Calculate the number of cans Mark brought in
    mark_cans = jaydon_cans * 4

    result = mark_cans
    return result

print(solution())