def solution():
    """Stephanie needs to figure out how many pieces of silverware she should purchase. She needs spoons, butter knives, steak knives, and forks. For herself she figures 5 of each would be sufficient. But in case she has guests, she wants to have 10 extra pieces of each type. Then she realizes that if everything is clean at the same time, that she will have too many of everything and not enough room to fit them in her kitchen silverware drawer. So she decides to purchase 4 fewer spoons, 4 fewer butter knives, 5 fewer steak knives, and 3 fewer forks. How many pieces total of all the silverware is Stephanie going to buy?"""
    
    # Define the initial number of silverware pieces Stephanie wants to buy
    initial_sp = 5
    initial_bk = 5
    initial_sk = 5
    initial_fork = 5
    
    # Define the additional silverware pieces Stephanie wants to buy in case of guests
    extra_sp = 10
    extra_bk = 10
    extra_sk = 10
    extra_fork = 10
    
    # Calculate the total number of silverware pieces Stephanie will buy without adjustment
    total_initial = (initial_sp + extra_sp) + (initial_bk + extra_bk) + (initial_sk + extra_sk) + (initial_fork + extra_fork)
    
    # Calculate the adjusted number of silverware pieces for each type
    adjusted_sp = initial_sp - 4
    adjusted_bk = initial_bk - 4
    adjusted_sk = initial_sk - 5
    adjusted_fork = initial_fork - 3
    
    # Calculate the total number of silverware pieces Stephanie will buy with adjustment
    total_adjusted = (adjusted_sp + extra_sp) + (adjusted_bk + extra_bk) + (adjusted_sk + extra_sk) + (adjusted_fork + extra_fork)
    
    # Display the total number of silverware pieces Stephanie will buy
    result = total_adjusted
    
    return result

print(solution())