def solution():
    """Since it is Maurice's turn to host this year’s neighborhood cookout, he goes to the local wholesale club to buy ground beef. The wholesale club sells ground beef in 5-pound packages. Maurice wants to make one 2-pound burger for each person that attends, so he purchases 4 packages of ground beef. How many people can Maurice invite to the cookout so that everybody, including himself, gets a burger?"""
    beef_package_size = 5
    beef_packages = 4
    beef_total = beef_package_size * beef_packages
    burger_size = 2
    burger_count = beef_total // burger_size
    # Maurice counts as a person, so add one to the total
    result = burger_count + 1
    return result

print(solution())