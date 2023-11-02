def solution():
    
    # Define the total amount of equipment bought
    total_equipment = 400000

    # Calculate the number of faulty pieces of equipment
    faulty_equipment = total_equipment * 0.4

    # Calculate the total amount spent on functioning pieces of equipment
    functioning_equipment = total_equipment - faulty_equipment

    # Display the total amount spent on functioning pieces of equipment
    result = functioning_equipment
    return result

print(solution())