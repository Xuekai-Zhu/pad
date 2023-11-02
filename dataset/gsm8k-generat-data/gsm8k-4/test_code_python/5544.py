def solution():
    """An agricultural cooperative must ship 6500 kg of potatoes. During transport by truck, 150 kg are damaged and therefore cannot be sold. The potatoes are distributed in 50 kg bags, each bag being sold for $72. What will the sale of the potatoes bring?"""
    # Define the total amount of potatoes to be sold
    total_potatoes = 6500 - 150

    # Calculate the number of bags of potatoes
    num_bags = total_potatoes // 50

    # Calculate the total revenue from selling the potatoes
    revenue = num_bags * 72

    result = revenue
    return result

print(solution())