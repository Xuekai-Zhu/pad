def solution():
    num_bags = 10
    oranges_per_bag = 30
    total_oranges = num_bags * oranges_per_bag
    rotten_oranges = 50
    oranges_for_juice = 30

    # Calculate the number of oranges that will be sold
    oranges_for_sale = total_oranges - (rotten_oranges + oranges_for_juice)
    result = oranges_for_sale
    return result

print(solution())