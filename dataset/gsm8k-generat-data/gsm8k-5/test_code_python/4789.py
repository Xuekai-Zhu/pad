def solution():
    packages_of_ground_beef = 4  # Maurice purchases 4 packages of ground beef
    weight_per_package = 5  # Each package of ground beef weighs 5 pounds
    burgers_per_package = weight_per_package / 2  # Maurice can make 2-pound burgers from each package of ground beef

    # Calculate the total number of burgers Maurice can make
    total_burgers = packages_of_ground_beef * burgers_per_package

    # Deduct one burger for Maurice himself
    total_burgers -= 1

    result = total_burgers
    return result

print(solution())