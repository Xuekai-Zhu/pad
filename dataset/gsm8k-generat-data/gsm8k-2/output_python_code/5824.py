def solution():
    """To make fried green tomatoes, Thelma cuts each green tomato into 8 slices before cooking them up. If 20 slices of fried green tomato make a meal for a single person, how many tomatoes will Thelma need to make enough fried green tomatoes to feed a family of 8 for a single meal?"""
    slices_per_tomato = 8
    slices_per_person = 20
    people_to_feed = 8
    total_slices_needed = slices_per_person * people_to_feed
    tomatoes_needed = total_slices_needed / slices_per_tomato
    result = tomatoes_needed
    return result

print(solution())