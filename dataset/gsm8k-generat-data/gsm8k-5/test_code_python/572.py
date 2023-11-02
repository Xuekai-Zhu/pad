def solution():
    target_income = 100  # Steve wants to make $100 in four days
    monday_income = 2 * 8  # Steve picked 8 pounds of lingonberries on Monday and earned $2 for each of them
    tuesday_income = 2 * (3 * 8)  # Steve picked triple the amount he picked on Monday on Tuesday
    wednesday_income = 0  # Steve rested on Wednesday and did not earn any money

    # Calculate the total income Steve has earned in three days
    total_income = monday_income + tuesday_income + wednesday_income

    # Calculate how much money Steve needs to make on Thursday to reach his target income
    thursday_income = target_income - total_income
    pounds_to_pick = thursday_income / 2  # Steve earns $2 for each pound of lingonberries picked

    result = pounds_to_pick
    return result

print(solution())