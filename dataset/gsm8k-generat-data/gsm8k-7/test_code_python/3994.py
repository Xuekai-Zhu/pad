def solution():
    num_packages = 10
    cars_per_package = 5
    num_nephews = 2
    nephew_share = (num_packages * cars_per_package) / num_nephews

    # Calculate the number of cars left with Tom
    num_cars_left = (num_packages * cars_per_package) - nephew_share * 2
    result = num_cars_left
    return result

print(solution())