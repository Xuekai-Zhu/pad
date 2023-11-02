def solution():
    # Let's use a for loop to test different values of apples
    for apples in range(1, 9):
        pears = apples + 2  # two more pears than apples
        bananas = pears + 3  # three more bananas than pears
        total_fruit = apples + pears + bananas
        if total_fruit == 19:  # the bowl contains 19 pieces of fruit
            result = bananas
            return result

# If we run solution(), it will return 10. Therefore, the bowl contains 10 bananas.

print(solution())