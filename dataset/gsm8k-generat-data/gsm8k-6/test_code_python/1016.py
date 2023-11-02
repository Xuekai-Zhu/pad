def solution():
    total_fruit = 78  # total number of fruit in the crate
    kiwi_fruit = total_fruit // 3  # one-third of the fruit are kiwi berries
    strawberry_fruit = total_fruit - kiwi_fruit  # the remaining fruit are strawberries
    result = strawberry_fruit
    return result

print(solution())