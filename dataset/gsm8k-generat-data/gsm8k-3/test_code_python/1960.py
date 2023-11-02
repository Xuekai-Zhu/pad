def solution():
    """ There are 10 bags with 30 oranges each on a truck. A total of 50 pieces of oranges are rotten. Thirty pieces of oranges will be kept for making orange juice and the rest will be sold. How many pieces of oranges will be sold? """
    # Define the number of bags and oranges per bag
    bags = 10
    oranges_per_bag = 30

    # Calculate the total number of oranges
    total_oranges = bags * oranges_per_bag

    # Subtract the number of rotten oranges and oranges for juice
    sellable_oranges = total_oranges - 50 - 30

    # Display the number of oranges to be sold
    result = sellable_oranges
    return result

print(solution())