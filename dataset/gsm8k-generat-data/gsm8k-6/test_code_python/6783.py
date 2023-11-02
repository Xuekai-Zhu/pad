def solution():
    # Calculate the total cost of a sandwich and a pack of juice
    total_cost = 0.3 + 0.2  

    # Calculate the number of friends Lyle can buy for with $2.50
    num_friends = int((2.5 - total_cost) / total_cost) 
    result = num_friends
    return result

print(solution())