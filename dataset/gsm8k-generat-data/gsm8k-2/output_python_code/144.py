def solution():
    """The owner of a Turkish restaurant wanted to prepare traditional dishes for an upcoming celebration. She ordered ground beef, in four-pound packages, from three different butchers. The following morning, the first butcher delivered 10 packages. A couple of hours later, 7 packages arrived from the second butcher. Finally, the third butcher’s delivery arrived at dusk. If all the ground beef delivered by the three butchers weighed 100 pounds, how many packages did the third butcher deliver?"""
    package_weight = 4
    total_weight = 100
    first_delivery = 10 * package_weight
    second_delivery = 7 * package_weight
    third_delivery = total_weight - first_delivery - second_delivery
    packages_delivered = third_delivery / package_weight
    result = packages_delivered
    return result

print(solution())