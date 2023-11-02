def solution():
    # Calculate the total number of tomatoes
    total_tomatoes = 18 * 7

    # Calculate the number of tomatoes that are dried
    dried_tomatoes = total_tomatoes / 2

    # Calculate the number of remaining tomatoes
    remaining_tomatoes = total_tomatoes - dried_tomatoes

    # Calculate the number of tomatoes turned into marinara sauce
    marinara_tomatoes = remaining_tomatoes / 3

    # Calculate the final number of tomatoes
    final_tomatoes = remaining_tomatoes - marinara_tomatoes
    result = final_tomatoes
    return result

print(solution())