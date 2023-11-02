def solution():
    """There are 35 bottles of milk on the grocery store shelf. Jason buys 5 of the bottles and Harry buys 6 more. How many bottles of milk are left on the store shelf after Jason and Harry purchased milk?"""
    # Define the initial number of bottles on the shelf
    initial_bottles = 35

    # Define the number of bottles purchased by Jason and Harry
    jason_purchased = 5
    harry_purchased = 6

    # Calculate the remaining number of bottles on the shelf
    remaining_bottles = initial_bottles - jason_purchased - harry_purchased

    # Display the remaining number of bottles
    result = remaining_bottles
    return result

print(solution())