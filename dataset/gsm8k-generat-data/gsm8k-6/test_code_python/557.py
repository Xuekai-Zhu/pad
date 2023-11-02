def solution():
    # Calculate the total number of tomatoes harvested
    total_tomatoes = 18 * 7

    # Calculate the number of tomatoes that are dried
    dried_tomatoes = total_tomatoes / 2

    # Calculate the number of tomatoes remaining after drying
    remaining_tomatoes = total_tomatoes - dried_tomatoes

    # Calculate the number of tomatoes that are turned into marinara sauce
    sauce_tomatoes = remaining_tomatoes / 3

    # Calculate the number of tomatoes left after making sauce
    final_tomatoes = remaining_tomatoes - sauce_tomatoes

    result = final_tomatoes
    return result

print(solution())