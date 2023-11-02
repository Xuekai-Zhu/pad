def solution():
    # Calculate the number of calories in half a package of candy
    calories_per_serving = 120
    servings_in_package = 3
    half_package_servings = servings_in_package / 2
    calories_in_half_package = calories_per_serving * half_package_servings
    result = calories_in_half_package
    return result

print(solution())