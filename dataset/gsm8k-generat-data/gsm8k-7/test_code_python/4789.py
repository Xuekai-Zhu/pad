def solution():
    package_size = 5  # pounds per package
    num_packages = 4
    servings_per_package = package_size / 2  # 2-pound burgers
    num_servings = num_packages * servings_per_package
    num_people = num_servings + 1  # Maurice also gets a burger
    result = num_people
    return result

print(solution())