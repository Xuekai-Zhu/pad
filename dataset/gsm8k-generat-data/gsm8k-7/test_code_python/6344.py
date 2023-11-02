def solution():
    num_jars = 5
    jar_capacity = 2  # in liters
    glass_capacity = 0.25  # in liters

    # Calculate the total amount of juice in liters
    total_juice = num_jars * jar_capacity

    # Calculate the total number of full glasses of juice that can be served
    num_glasses = total_juice / glass_capacity

    result = int(num_glasses)
    return result

print(solution())