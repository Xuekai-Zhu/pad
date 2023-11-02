def solution():
    """Since it is Maurice's turn to host this year’s neighborhood cookout, he goes to the local wholesale club to buy ground beef. The wholesale club sells ground beef in 5-pound packages. Maurice wants to make one 2-pound burger for each person that attends, so he purchases 4 packages of ground beef. How many people can Maurice invite to the cookout so that everybody, including himself, gets a burger?"""
    # Define the number of packages of ground beef purchased
    num_packages = 4

    # Define the weight of each package of ground beef
    package_weight = 5

    # Calculate the total weight of ground beef purchased
    total_weight = num_packages * package_weight

    # Calculate the number of burgers that can be made
    num_burgers = total_weight // 2

    # Calculate the number of people that can be invited
    num_people = num_burgers + 1 # Maurice included

    result = num_people
    return result

print(solution())