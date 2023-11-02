def solution():
    """Mr. Shaefer harvested 500 lychees in a carton and took them to the market. 
    He sold half of them and took home the remaining number of lychees where 
    they ate 3/5 of them. Calculate the number of lychees remaining."""
    
    # Define the number of lychees harvested
    carton_size = 500
    
    # Calculate the number of lychees sold
    sold = carton_size/2
    
    # Calculate the number of lychees taken home
    remaining = carton_size - sold
    
    # Calculate the number of lychees eaten at home
    eaten = remaining * 3/5
    
    # Calculate the number of lychees remaining
    remaining = remaining - eaten
    
    result = remaining
    return result

print(solution())