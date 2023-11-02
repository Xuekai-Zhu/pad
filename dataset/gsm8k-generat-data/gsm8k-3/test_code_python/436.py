def solution():
    """Catherine had an equal number of pencils and pens. If she had 60 pens and gave eight pens and 6 pencils to each of her seven friends and kept the rest for herself, how many pens and pencils did she have left?"""
    # Define the number of initial pens and pencils
    initial_quantity = 60

    # Calculate the total number of items given to friends
    items_given = (8 + 6) * 7

    # Calculate the remaining number of items for Catherine
    remaining_items = initial_quantity - items_given

    # Divide the remaining items equally between pens and pencils
    remaining_pens = remaining_items / 2
    remaining_pencils = remaining_items / 2

    # Display the remaining pens and pencils
    result = (remaining_pens, remaining_pencils)
    return result

print(solution())