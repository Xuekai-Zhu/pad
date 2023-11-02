def solution():
    """Since it is Maurice's turn to host this year’s neighborhood cookout, he goes to the local wholesale club to buy ground beef. The wholesale club sells ground beef in 5-pound packages. Maurice wants to make one 2-pound burger for each person that attends, so he purchases 4 packages of ground beef. How many people can Maurice invite to the cookout so that everybody, including himself, gets a burger?"""
    
    # Define the weight of each ground beef package
    PACKAGE_WEIGHT = 5

    # Define the weight of each burger
    BURGER_WEIGHT = 2

    # Define the number of ground beef packages purchased
    packages_purchased = 4

    # Calculate the total amount of ground beef purchased in pounds
    total_ground_beef = packages_purchased * PACKAGE_WEIGHT

    # Calculate the maximum number of burgers that can be made
    max_burgers = total_ground_beef // BURGER_WEIGHT

    # Calculate the maximum number of people that can be invited to the cookout
    max_people = max_burgers - 1

    # Display the maximum number of people
    result = max_people
    return result

print(solution())