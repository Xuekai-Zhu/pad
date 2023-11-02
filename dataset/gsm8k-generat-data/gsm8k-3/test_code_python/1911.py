def solution():
    """If Brooke adds eight balloons to his current 12, and Tracy adds 24 to her current 6, how many balloons will they have in total if Tracy pops half of her balloons?"""
    # Define Brooke's initial number of balloons and the number he adds
    brooke_start = 12
    brooke_add = 8

    # Define Tracy's initial number of balloons and the number she adds
    tracy_start = 6
    tracy_add = 24

    # Calculate the total number of balloons before Tracy pops any
    total_balloons = brooke_start + brooke_add + tracy_start + tracy_add

    # Calculate the number of balloons Tracy pops
    tracy_pops = tracy_add / 2

    # Calculate the final number of balloons
    final_balloons = total_balloons - tracy_pops

    # Display the final number of balloons
    result = final_balloons
    return result

print(solution())