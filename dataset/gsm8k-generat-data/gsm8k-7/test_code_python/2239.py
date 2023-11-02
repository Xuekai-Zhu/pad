def solution():
    betty_oranges = 15
    bill_oranges = 12
    frank_oranges = (betty_oranges + bill_oranges) * 3
    
    num_seeds_per_orange = 2
    num_years = 20
    num_oranges_per_tree = 5
    
    # Calculate the total number of oranges that Philip can pick
    total_oranges = (frank_oranges * num_seeds_per_orange * num_years) + (betty_oranges + bill_oranges)
    
    # Calculate the total number of orange trees
    num_trees = frank_oranges * num_seeds_per_orange
    
    # Calculate the total number of oranges per tree
    total_oranges_per_tree = num_oranges_per_tree * num_years
    
    # Calculate the total number of oranges for Philip to pick
    total_oranges_for_philip = total_oranges_per_tree * num_trees
    
    result = total_oranges_for_philip
    return result

print(solution())