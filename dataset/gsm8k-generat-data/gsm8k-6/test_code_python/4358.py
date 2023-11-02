def solution():
    # Calculate the total number of slices needed
    total_slices = 20 * desired_slices  # desired_slices is the number of slices each child will receive
    for slices in [6, 8, 10]:  # check each option for the number of slices per pizza
        if total_slices % slices == 0:  # if the total number of slices can be evenly divided by the number of slices per pizza
            desired_slices = total_slices // (5 * slices)  # calculate the desired number of slices per child
            result = slices
            return result

print(solution())