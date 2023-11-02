def solution():
    # Calculate the total number of strawberries and tomatoes harvested
    total_strawberries = 5 * 14
    total_tomatoes = 7 * 16

    # Calculate the number of baskets of strawberries and tomatoes
    baskets_of_strawberries = total_strawberries // 7
    baskets_of_tomatoes = total_tomatoes // 7

    # Calculate the total amount of money earned
    money_from_strawberries = baskets_of_strawberries * 9
    money_from_tomatoes = baskets_of_tomatoes * 6
    total_money = money_from_strawberries + money_from_tomatoes

    result = total_money
    return result

print(solution())