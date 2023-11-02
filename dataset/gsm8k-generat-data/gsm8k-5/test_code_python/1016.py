def solution():
    total_fruit = 78  # There are 78 pieces of fruit in the crate
    kiwi = total_fruit / 3  # One-third of the box contains kiwi
    strawberries = total_fruit - kiwi  # The rest are strawberries
    result = strawberries
    return result

print(solution())