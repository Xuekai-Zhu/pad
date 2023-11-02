def solution():
    """Emma bought a loaf of bread that had a certain number of slices. Her little cousin Andy ate 3 slices from the bread at two different points in time, and then Emma decided she would make toast with the remaining slices. If she uses 2 slices of bread to make 1 piece of toast bread, how many slices were in the original loaf if she was able to make 10 pieces of toast bread and had 1 slice of bread left?"""
    # Define the number of slices eaten by Andy
    andy_slices = 6

    # Define the number of slices remaining
    remaining_slices = None

    # Define the number of slices used to make toast
    toast_slices = 20

    # Calculate the total number of slices in the original loaf
    total_slices = andy_slices + remaining_slices + toast_slices + 1

    # Check how many slices were in the original loaf
    for i in range(1, total_slices):
        # Calculate the remaining slices after Andy ate
        remaining_slices = total_slices - andy_slices

        # Calculate the number of slices used to make toast
        toast_slices = remaining_slices // 2

        # Calculate the final number of slices
        final_slices = remaining_slices - toast_slices

        # Check if it matches the given conditions
        if final_slices == 1 and toast_slices == 10:
            result = total_slices
            return result

    # If no solution is found
    return "No solution found."

print(solution())