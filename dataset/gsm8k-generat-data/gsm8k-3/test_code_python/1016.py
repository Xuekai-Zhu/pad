def solution():
    """There are 78 pieces of fruit in a crate. One-third of the box contains kiwi. The rest are strawberries. How many strawberries are there?"""
    # Define the total number of fruit in the crate
    total_fruit = 78

    # Calculate the number of kiwi
    kiwi = total_fruit // 3

    # Calculate the number of strawberries
    strawberries = total_fruit - kiwi

    # Display the number of strawberries
    result = strawberries
    return result

print(solution())