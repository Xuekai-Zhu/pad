def solution():
    """Tom decides to make lasagna with all his beef.  It takes twice as many noodles as beef.  He has 10 pounds of beef.  He already has 4 pounds of lasagna noodles and the noodles come in 2-pound packages.  How many packages does he need to buy?"""
    # Define the ratio of beef to noodles
    BEEF_TO_NOODLES = 1
    NOODLES_TO_BEEF = 2

    # Define the weight of beef and noodles
    beef_weight = 10
    noodle_weight = beef_weight * NOODLES_TO_BEEF

    # Add the weight of the noodles Tom already has
    noodle_weight += 4

    # Calculate the number of noodle packages needed
    noodle_packages = (noodle_weight // 2) + (noodle_weight % 2 > 0)

    # Display the number of noodle packages needed
    result = noodle_packages
    return result

print(solution())