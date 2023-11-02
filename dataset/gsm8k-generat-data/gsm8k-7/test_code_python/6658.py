def solution():
    apples_tuesday = 4
    apples_wednesday = 2 * apples_tuesday
    apples_thursday = apples_tuesday / 2

    # Calculate the total number of apples that Anna ate over three days
    total_apples = apples_tuesday + apples_wednesday + apples_thursday
    result = total_apples
    return result

print(solution())