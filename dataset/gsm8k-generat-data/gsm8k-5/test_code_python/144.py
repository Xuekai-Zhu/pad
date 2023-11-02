def solution():
    package_weight = 4  # Each package of ground beef weighs 4 pounds
    total_weight = 100  # The total weight of all ground beef delivered is 100 pounds

    # Calculate the total number of packages delivered by the first two butchers
    packages_first_two = (10 + 7) * package_weight

    # Calculate the number of packages delivered by the third butcher
    packages_third = (total_weight - packages_first_two) / package_weight
    result = packages_third
    return result

print(solution())