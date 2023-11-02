def solution():
    total_fruit = 10 + 5  # Total fruit in the basket before Emily adds more oranges
    total_fruit_after_adding_oranges = total_fruit + 5  # Total fruit after Emily adds 5 more oranges
    percentage_of_apples = (10 / total_fruit_after_adding_oranges) * 100

    result = percentage_of_apples
    return result

print(solution())