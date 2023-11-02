def solution():
    # Calculate the total number of sweet potatoes not yet sold
    total_potatoes = 80  # total number of sweet potatoes harvested
    sold_potatoes = 20 + 15  # number of sweet potatoes sold to Mrs. Adams and Mr. Lenon
    remaining_potatoes = total_potatoes - sold_potatoes  # number of sweet potatoes not yet sold
    result = remaining_potatoes
    return result

print(solution())