def solution():
    """There are 78 pieces of fruit in a crate. One-third of the box contains kiwi. The rest are strawberries. How many strawberries are there?"""
    # Define the total number of fruit in the crate
    total_fruit = 78

    # Calculate the number of kiwi fruit in the crate
    kiwi_fruit = total_fruit // 3

    # Calculate the number of strawberries in the crate
    strawberry_fruit = total_fruit - kiwi_fruit

    # return the result
    result = strawberry_fruit
    return result

print(solution())