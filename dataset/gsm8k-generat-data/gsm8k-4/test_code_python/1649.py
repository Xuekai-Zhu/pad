def solution():
    """In a field of 500 clovers, 20% have four leaves and one quarter of these are purple clovers. Assuming these proportions are exactly correct, how many clovers in the field are both purple and four-leaved?"""
    # Define the total number of clovers and the percentage of four-leaved clovers
    total_clovers = 500
    four_leaved_percentage = 0.2

    # Calculate the number of four-leaved clovers
    four_leaved_clovers = total_clovers * four_leaved_percentage

    # Calculate the number of purple clovers
    purple_clovers = four_leaved_clovers * 0.25

    # Round the result to the nearest integer
    result = round(purple_clovers)
    return result

print(solution())