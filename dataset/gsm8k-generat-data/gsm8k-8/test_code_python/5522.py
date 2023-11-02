def solution():
    # Define the total number of sweet potatoes
    total_potatoes = 80

    # Define the number of sweet potatoes sold to Mrs. Adams
    sold_to_adams = 20

    # Define the number of sweet potatoes sold to Mr. Lenon
    sold_to_lenon = 15

    # Calculate the number of sweet potatoes not yet sold
    not_sold = total_potatoes - sold_to_adams - sold_to_lenon

    result = not_sold
    return result

print(solution())