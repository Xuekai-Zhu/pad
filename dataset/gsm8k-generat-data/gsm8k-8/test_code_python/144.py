def solution():
    # Define the weight of one package
    package_weight = 4

    # Calculate the total number of packages delivered by the first two butchers
    first_butcher_packages = 10
    second_butcher_packages = 7
    total_packages = first_butcher_packages + second_butcher_packages

    # Calculate the total weight of the ground beef delivered by the first two butchers
    total_weight = total_packages * package_weight

    # Calculate the number of packages delivered by the third butcher
    third_butcher_packages = (100 - total_weight) / package_weight
    result = third_butcher_packages
    return result

print(solution())