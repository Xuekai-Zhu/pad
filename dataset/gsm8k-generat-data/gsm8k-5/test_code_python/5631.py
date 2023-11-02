def solution():
    # Calculate the total hours of classes Kim had before dropping a class
    total_hours = 4 * 2  # Kim has 4 classes, each lasting 2 hours

    # Calculate the hours of classes Kim has now after dropping 1 class
    remaining_classes = 3  # Kim dropped 1 class, so she has 3 remaining
    hours_per_day = total_hours / remaining_classes

    result = hours_per_day
    return result

print(solution())