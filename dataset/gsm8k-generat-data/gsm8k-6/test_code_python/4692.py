def solution():
    # Calculate the total money earned from raking leaves on Monday and Tuesday
    total_money = 4*5 + 4*3  # they charge $4 for each bag of leaves they rake
    money_on_wednesday = 68 - total_money  # calculate the money earned on Wednesday
    bags_on_wednesday = money_on_wednesday / 4  # each bag costs $4
    result = bags_on_wednesday
    return result

print(solution())