def solution():
    # Calculate the total number of animals Aubree saw on her way to school
    initial_total = 20 + 40

    # Calculate the new total number of animals on her way back from school
    final_beavers = 20 * 2
    final_chipmunks = 40 - 10
    final_total = final_beavers + final_chipmunks

    # Calculate the overall total number of animals Aubree saw that day
    overall_total = initial_total + final_total
    result = overall_total
    return result

print(solution())