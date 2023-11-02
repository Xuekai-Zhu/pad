def solution():
    num_clotheslines_per_house = 2
    num_children = 11
    num_adults = 20
    num_child_items = 4
    num_adult_items = 3
    num_items_per_clothesline = 2

    # Calculate the total number of items of clothing on the clotheslines
    total_items = (num_children * num_child_items) + (num_adults * num_adult_items)

    # Calculate the total number of clotheslines needed
    num_clotheslines_needed = total_items / num_items_per_clothesline

    # Calculate the total number of houses on the street
    num_houses = num_clotheslines_needed / num_clotheslines_per_house

    result = num_houses
    return result

print(solution())