def solution():
    # Calculate the amount of noodles needed for the lasagna
    noodles_needed = 2 * 10  # it takes twice as many noodles as beef

    # Calculate the number of packages of noodles Tom needs to buy
    packages_needed = (noodles_needed - 4) / 2  # he already has 4 pounds of noodles, and the noodles come in 2-pound packages

    result = packages_needed
    return result

print(solution())