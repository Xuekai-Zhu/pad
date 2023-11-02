def solution():
    # Calculate the amount of garbage accumulated during the first week
    first_week_garbage = 3 * 200  # 3 collections, 200 kg each

    # Calculate the amount of garbage accumulated during the second week
    second_week_garbage = 1.5 * 3 * 200  # 1.5 amount of garbage during one week

    # Calculate the total amount of accumulated garbage
    total_garbage = first_week_garbage + second_week_garbage
    result = total_garbage
    return result

print(solution())