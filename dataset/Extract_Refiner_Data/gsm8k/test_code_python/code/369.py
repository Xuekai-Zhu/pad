def solution():
    
    # Define the total cost of the equipment
    total_cost = 400000

    # Calculate the number of faulty pieces of equipment
    num_faulty = total_cost * 0.4

    # Calculate the cost of the functioning pieces of equipment
    num_functioning = total_cost - num_faulty

    # Display the cost of the functioning pieces of equipment
    result = num_functioning
    return result

print(solution())