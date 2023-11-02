def solution():
    """Since it is Maurice's turn to host this year’s neighborhood cookout, he goes to the local wholesale club to buy ground beef. The wholesale club sells ground beef in 5-pound packages. Maurice wants to make one 2-pound burger for each person that attends, so he purchases 4 packages of ground beef. How many people can Maurice invite to the cookout so that everybody, including himself, gets a burger?"""
    beef_per_package = 5
    total_beef = beef_per_package * 4
    beef_per_burger = 2
    total_burgers = total_beef // beef_per_burger
    people = total_burgers + 1
    result = people
    return result

print(solution())