def solution():
    max_weight = 20  # Maximum weight the grocery bag can hold is 20 pounds
    current_weight = 4 + 6 + (2 * 4)  # Mary has bought 4 pounds of green beans, 6 pounds of milk, and 8 pounds of carrots (2*4)
    remaining_weight = max_weight - current_weight  # Calculate the weight of groceries that can still fit in the bag
    result = remaining_weight
    return result

print(solution())