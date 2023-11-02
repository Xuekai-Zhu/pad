def solution():
    """Mark is looking to buy a total of 12 pieces of fruit at the store. He has already chosen 3 apples. He has also selected a bunch of bananas containing 4 bananas. How many oranges does he need to pick out to have 12 total pieces of fruit?"""
    # Define the number of apples and bananas already chosen
    num_apples = 3
    num_bananas = 4

    # Define the total number of fruit Mark wants to buy
    total_fruit = 12

    # Calculate the number of oranges needed to reach the total
    num_oranges = total_fruit - num_apples - num_bananas

    # Display the number of oranges needed
    result = num_oranges
    return result

print(solution())