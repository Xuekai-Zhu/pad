def solution():
    # Define the number of days and servings per bottle
    num_days = 180
    servings_per_bottle = 60 * 2

    # Calculate the total number of servings needed
    total_servings = num_days * 1

    # Calculate the number of bottles needed
    num_bottles = total_servings / servings_per_bottle
    result = round(num_bottles)
    return result

print(solution())