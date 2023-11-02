def solution():
    """There are 35 bottles of milk on the grocery store shelf. Jason buys 5 of the bottles and Harry buys 6 more. How many bottles of milk are left on the store shelf after Jason and Harry purchased milk?"""
    # Define the initial number of bottles on the shelf
    bottles_on_shelf = 35

    # Jason buys 5 bottles
    bottles_jason_buys = 5

    # Harry buys 6 more
    bottles_harry_buys = 6

    # Calculate the total number of bottles purchased
    total_bottles_purchased = bottles_jason_buys + bottles_harry_buys

    # Calculate the number of bottles left on the shelf
    bottles_left = bottles_on_shelf - total_bottles_purchased

    # return the result
    result = bottles_left
    return result

print(solution())