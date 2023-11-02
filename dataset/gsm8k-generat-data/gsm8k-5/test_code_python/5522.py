def solution():
    total_potatoes = 80  # Mrs. Lacson harvested 80 sweet potatoes
    sold_to_Adams = 20  # Mrs. Lacson sold 20 sweet potatoes to Mrs. Adams
    sold_to_Lenon = 15  # Mrs. Lacson sold 15 sweet potatoes to Mr. Lenon

    # Calculate the number of sweet potatoes not yet sold
    remaining_potatoes = total_potatoes - sold_to_Adams - sold_to_Lenon
    result = remaining_potatoes
    return result

print(solution())