def solution():
    """Mrs. Lacson harvested 80 sweet potatoes. She sold 20 of them to Mrs. Adams and 15 of them to Mr. Lenon. How many sweet potatoes are not yet sold?"""
    # Define the total number of harvested sweet potatoes
    total_potatoes = 80

    # Calculate the number of sweet potatoes sold to Mrs. Adams and Mr. Lenon
    sold_potatoes = 20 + 15

    # Calculate the number of sweet potatoes not yet sold
    remaining_potatoes = total_potatoes - sold_potatoes

    # return the result
    result = remaining_potatoes
    return result

print(solution())