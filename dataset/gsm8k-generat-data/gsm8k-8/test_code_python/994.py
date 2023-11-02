def solution():
    # Calculate total number of slices
    total_slices = 2 * 12

    # Calculate slices eaten by Dean and remaining slices
    dean_slices = 0.5 * 12
    remaining_slices = total_slices - dean_slices

    # Calculate slices eaten by Frank and remaining slices
    frank_slices = 3
    remaining_slices -= frank_slices

    # Calculate slices eaten by Sammy and remaining slices
    sammy_slices = (1/3) * (2 * 12)
    remaining_slices -= sammy_slices

    result = remaining_slices
    return result

print(solution())