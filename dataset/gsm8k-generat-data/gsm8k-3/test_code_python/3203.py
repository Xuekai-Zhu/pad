def solution():
    """The cost of transporting 80 bags of cement, each weighing 50 kgs, is $6000. What's the cost of transporting three times as many cement bags, each weighing 3/5 times as many kgs?"""
    # Define the cost of transporting the original 80 bags of cement
    original_cost = 6000

    # Define the weight of each bag of cement in kgs
    original_weight = 50

    # Define the number of bags of cement in the new shipment
    new_bags = 3 * 80

    # Define the weight of each bag of cement in the new shipment
    new_weight = original_weight * (3/5)

    # Calculate the total weight of the new shipment
    total_weight = new_bags * new_weight

    # Calculate the cost of transporting the new shipment
    new_cost = (total_weight/1000) * 120

    # Display the cost of transporting the new shipment
    result = new_cost
    return result

print(solution())