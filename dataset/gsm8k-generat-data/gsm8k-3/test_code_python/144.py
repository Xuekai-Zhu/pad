def solution():
    """The owner of a Turkish restaurant wanted to prepare traditional dishes for an upcoming celebration. She ordered ground beef, in four-pound packages, from three different butchers. The following morning, the first butcher delivered 10 packages. A couple of hours later, 7 packages arrived from the second butcher. Finally, the third butcher’s delivery arrived at dusk. If all the ground beef delivered by the three butchers weighed 100 pounds, how many packages did the third butcher deliver?"""
    # Define the weight of each package of ground beef
    PACKAGE_WEIGHT = 4

    # Calculate the total number of packages delivered by the first two butchers
    first_butcher_packages = 10
    second_butcher_packages = 7
    total_packages_delivered = first_butcher_packages + second_butcher_packages

    # Calculate the total weight of ground beef delivered by the first two butchers
    total_weight_delivered = total_packages_delivered * PACKAGE_WEIGHT

    # Calculate the weight of ground beef delivered by the third butcher
    third_butcher_weight = 100 - total_weight_delivered

    # Calculate the number of packages delivered by the third butcher
    third_butcher_packages = third_butcher_weight / PACKAGE_WEIGHT

    # Round up the number of packages to the nearest whole number
    third_butcher_packages = round(third_butcher_packages)

    result = third_butcher_packages
    return result

print(solution())