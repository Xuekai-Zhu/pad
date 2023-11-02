def solution():
    # Calculate the number of strawberries
    num_strawberries = (3/5) * 100

    # Calculate the total number of fruits
    total_fruits = 100 + num_strawberries

    # Calculate the number of fruits given to each friend
    each_friend = (1/5) * total_fruits

    # Calculate the total number of fruits left
    fruits_left = total_fruits - 2*each_friend

    result = fruits_left
    return result

print(solution())