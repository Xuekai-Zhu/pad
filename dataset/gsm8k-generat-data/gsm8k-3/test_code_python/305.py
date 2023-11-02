def solution():
    """Tommy is making 12 loaves of bread. He needs 4 pounds of flour per loaf. A 10-pound bag of flour costs $10 and a 12-pound bag costs $13. When he is done making his bread, he has no use for flour and so he will throw away whatever is left. How much does he spend on flour if he buys the cheapest flour to get enough?"""
    # Define the amount of flour needed and the prices of the flour bags
    flour_per_loaf = 4
    bag10_price = 10
    bag10_weight = 10
    bag12_price = 13
    bag12_weight = 12

    # Calculate the total amount of flour needed
    total_flour = 12 * flour_per_loaf

    # Calculate the number of bags of each type of flour needed
    bags10_needed = total_flour // bag10_weight + (total_flour % bag10_weight != 0)
    bags12_needed = total_flour // bag12_weight + (total_flour % bag12_weight != 0)

    # Calculate the cost of each type of flour needed
    cost10 = bags10_needed * bag10_price
    cost12 = bags12_needed * bag12_price

    # Determine which type of flour to purchase and calculate the total cost
    if cost10 < cost12:
        total_cost = cost10
    else:
        total_cost = cost12

    # Display the total cost
    result = total_cost
    return result

print(solution())