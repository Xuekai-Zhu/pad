def solution():
    """On Friday, Remy paid Sally’s Woodworking LLC a total of $20,700 for 150 pieces of furniture. Later that evening, the company’s accountant discovered that a new intern in the sales department had overcharged Remy. If the cost of a piece of furniture is $134, how much money will Sally’s Woodworking LLC reimburse Remy?"""
    # Define the total cost and number of furniture pieces paid for
    total_cost = 20700
    num_pieces = 150

    # Calculate the actual cost per piece of furniture
    actual_cost = total_cost / num_pieces

    # Calculate the overcharge per piece of furniture
    overcharge = actual_cost - 134

    # Calculate the total overcharge for all pieces of furniture
    total_overcharge = overcharge * num_pieces

    # Display the total amount that Sally's Woodworking LLC needs to reimburse Remy
    result = total_overcharge
    return result

print(solution())