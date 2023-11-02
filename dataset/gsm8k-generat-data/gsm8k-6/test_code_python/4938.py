def solution():
    # Calculate the number of undamaged cartons that each customer received
    undamaged_cartons_per_customer = (400 - 60) / 4  
    # Calculate the total number of undamaged cartons accepted by all customers
    total_undamaged_cartons = undamaged_cartons_per_customer * 4  
    result = total_undamaged_cartons
    return result

print(solution())