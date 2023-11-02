def solution():
    # Calculate the total number of strawberries and tomatoes harvested
    total_strawberries = 5 * 14
    total_tomatoes = 7 * 16

    # Calculate the number of baskets of strawberries and tomatoes
    baskets_strawberries = total_strawberries // 7
    baskets_tomatoes = total_tomatoes // 7

    # Calculate the total amount of money made by Nathan
    total_money = baskets_strawberries * 9 + baskets_tomatoes * 6
    result = total_money
    return result

print(solution())