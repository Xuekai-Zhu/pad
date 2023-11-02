def solution():
    # Calculate the total weight of ground beef delivered by the first two butchers
    first_delivery_weight = 10 * 4  # 10 packages, each of which contains 4 pounds of ground beef
    second_delivery_weight = 7 * 4  # 7 packages, each of which contains 4 pounds of ground beef
    total_weight = 100  # total weight of all ground beef delivered

    # Calculate the weight of ground beef delivered by the third butcher
    third_delivery_weight = total_weight - first_delivery_weight - second_delivery_weight

    # Calculate the number of packages delivered by the third butcher
    third_delivery_packages = third_delivery_weight / 4  # each package contains 4 pounds of ground beef

    result = third_delivery_packages
    return result

print(solution())