def solution():
    """The owner of a Turkish restaurant wanted to prepare traditional dishes for an upcoming celebration. She ordered ground beef, in four-pound packages, from three different butchers. The following morning, the first butcher delivered 10 packages. A couple of hours later, 7 packages arrived from the second butcher. Finally, the third butcher’s delivery arrived at dusk. If all the ground beef delivered by the three butchers weighed 100 pounds, how many packages did the third butcher deliver?"""
    # Define the weight of one package of ground beef
    PACKAGE_WEIGHT = 4

    # Calculate the total number of packages delivered by the first two butchers
    packages_delivered = 10 + 7

    # Calculate the total weight of ground beef delivered by the first two butchers
    weight_delivered = packages_delivered * PACKAGE_WEIGHT

    # Calculate the weight of ground beef delivered by the third butcher
    weight_third = 100 - weight_delivered

    # Calculate the number of packages delivered by the third butcher
    packages_third = weight_third / PACKAGE_WEIGHT

    # return the result
    result = packages_third
    return result

print(solution())