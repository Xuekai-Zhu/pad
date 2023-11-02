def solution():
    num_grasshoppers_on_plant = 7
    num_dozen_baby_grasshoppers = 2
    num_baby_grasshoppers_per_dozen = 12

    # Calculate the total number of baby grasshoppers
    total_baby_grasshoppers = num_dozen_baby_grasshoppers * num_baby_grasshoppers_per_dozen

    # Calculate the total number of grasshoppers
    total_grasshoppers = num_grasshoppers_on_plant + total_baby_grasshoppers

    result = total_grasshoppers
    return result

print(solution())