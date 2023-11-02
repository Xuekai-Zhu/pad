def solution():
    """Raul had $87 to spare so he decided to go to the bookshop. Raul bought 8 comics, each of which cost $4. How much money does Raul have left?"""
    # Define the cost of each comic
    COMIC_PRICE = 4

    # Define the amount of money Raul had to start with
    starting_money = 87

    # Calculate the total cost of the comics
    total_cost = COMIC_PRICE * 8

    # Calculate the amount of money Raul has left
    remaining_money = starting_money - total_cost

    # Display the amount of money Raul has left
    result = remaining_money
    return result

print(solution())