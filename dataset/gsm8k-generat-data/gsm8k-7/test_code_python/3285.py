def solution():
    leila_bags = 2
    leila_toys_per_bag = 25

    mohamed_bags = 3
    mohamed_toys_per_bag = 19

    # Calculate the total number of toys that Leila donated
    leila_total_toys = leila_bags * leila_toys_per_bag

    # Calculate the total number of toys that Mohamed donated
    mohamed_total_toys = mohamed_bags * mohamed_toys_per_bag
    
    # Calculate the difference in the number of toys donated by Mohamed and Leila
    difference = mohamed_total_toys - leila_total_toys
    result = difference
    return result

print(solution())