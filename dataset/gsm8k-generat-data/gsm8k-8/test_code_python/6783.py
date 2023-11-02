def solution():
    # Define the cost of one sandwich and one pack of juice
    sandwich_cost = 0.30
    juice_cost = 0.20
    
    # Define Lyle's budget
    budget = 2.50
    
    # Calculate the maximum number of sandwiches Lyle can buy
    max_sandwiches = budget // sandwich_cost
    
    # Calculate the maximum number of packs of juice Lyle can buy
    max_juices = budget // juice_cost
    
    # Calculate the maximum number of friends that can have a sandwich and a pack of juice
    max_friends = min(max_sandwiches, max_juices)

    result = max_friends
    return result

print(solution())