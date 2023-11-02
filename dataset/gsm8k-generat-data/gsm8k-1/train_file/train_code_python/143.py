def solution():
    """The owner of a Turkish restaurant wanted to prepare traditional dishes for an upcoming celebration. She ordered ground beef, in four-pound packages, from three different butchers. The following morning, the first butcher delivered 10 packages. A couple of hours later, 7 packages arrived from the second butcher. Finally, the third butcher’s delivery arrived at dusk. If all the ground beef delivered by the three butchers weighed 100 pounds, how many packages did the third butcher deliver?"""
    package_weight = 4
    total_packages = 0
    for packages in range(1, 11):
        total_packages += packages
    for packages in range(1, 8):
        total_packages += packages
    total_weight = total_packages * package_weight
    third_butcher = (100 - total_weight) / package_weight
    result = third_butcher
    return result

print(solution())