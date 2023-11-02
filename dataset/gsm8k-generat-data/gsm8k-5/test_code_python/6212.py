def solution():
    daragh_bears = 20  # Daragh had 20 stuffed bears
    favorite_bears = 8  # Daragh took out her favorite 8 bears
    remaining_bears = daragh_bears - favorite_bears  # Daragh has 12 bears remaining
    sisters = 3  # Daragh has 3 sisters

    # Calculate the number of bears each sister gets
    bears_per_sister = remaining_bears // sisters

    eden_bears = bears_per_sister + 10  # Eden already had 10 bears
    result = eden_bears
    return result

print(solution())