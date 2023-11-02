def solution():
    bags_monday = 5  # Bob and Johnny raked 5 bags of leaves on Monday
    bags_tuesday = 3  # Bob and Johnny raked 3 bags of leaves on Tuesday
    total_money = 68  # Bob and Johnny made $68 in total for all three days
    bags_wednesday = (total_money - (4 * (bags_monday + bags_tuesday))) / 4  # Bob and Johnny charge $4 per bag of leaves

    result = bags_wednesday
    return result

print(solution())