def solution():
    # Calculate the total strawberries and tomatoes harvested
    total_strawberries = 5 * 14  # Nathan has 5 strawberry plants, each giving 14 strawberries
    total_tomatoes = 7 * 16  # Nathan has 7 tomato plants, each giving 16 tomatoes

    # Calculate the number of baskets of strawberries and tomatoes
    baskets_of_strawberries = total_strawberries // 7
    baskets_of_tomatoes = total_tomatoes // 7

    # Calculate the amount of money Nathan makes from his harvest
    income_from_strawberries = baskets_of_strawberries * 9  # Each basket of strawberries sells for $9
    income_from_tomatoes = baskets_of_tomatoes * 6  # Each basket of tomatoes sells for $6
    total_income = income_from_strawberries + income_from_tomatoes
    result = total_income
    return result

print(solution())