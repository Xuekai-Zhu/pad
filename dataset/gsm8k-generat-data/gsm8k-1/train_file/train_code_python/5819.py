def solution():
    """Mrs. Young makes bonnets for kids in the orphanage. On Monday, she made 10 bonnets, on Tuesday and Wednesday combined she made twice more than on Monday, while on Thursday she made 5 more than on Monday, and on Friday she made 5 less than on Thursday. Then, she divided up the bonnets evenly and sent them to 5 orphanages. How many bonnets did Mrs. Young send to each orphanage?"""
    monday_bonnets = 10
    tuesday_wednesday_bonnets = 2 * monday_bonnets
    thursday_bonnets = monday_bonnets + 5
    friday_bonnets = thursday_bonnets - 5
    total_bonnets = monday_bonnets + tuesday_wednesday_bonnets + thursday_bonnets + friday_bonnets
    bonnets_per_orphanage = total_bonnets // 5
    result = bonnets_per_orphanage
    return result

print(solution())