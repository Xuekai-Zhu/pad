def solution():
    """Mark is making a quadruple batch of brownies. The normal recipe calls for 3 cups of flour and 1 cup milk. If flour is sold in 2-cup bags and milk is sold in 2-cup bottles, how many more bags of flour than bottles of milk does Mark have to buy?"""
    batch_size = 4
    flour_per_batch = 3
    milk_per_batch = 1
    total_flour_needed = batch_size * flour_per_batch
    total_milk_needed = batch_size * milk_per_batch
    bags_of_flour_needed = (total_flour_needed + 1) // 2
    bottles_of_milk_needed = (total_milk_needed + 1) // 2
    difference = bags_of_flour_needed - bottles_of_milk_needed
    result = difference
    return result

print(solution())