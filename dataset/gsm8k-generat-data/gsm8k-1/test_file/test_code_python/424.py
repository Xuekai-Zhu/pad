def solution():
    """A food caterer was told to prepare gourmet hot dogs for 36 guests. While most people would only eat one hotdog, he prepared enough for half of the guests to be able to have two hotdogs. However, 40 guests showed up, and everyone wanted a second hotdog. How many guests did not get a second hotdog?"""
    initial_guests = 36
    double_hotdog_guests = initial_guests / 2
    total_hotdogs = initial_guests + double_hotdog_guests
    extra_guests = 40 - initial_guests
    total_second_hotdogs = total_hotdogs + extra_guests
    guests_without_second_hotdog = 40 - total_second_hotdogs
    result = guests_without_second_hotdog
    return result

print(solution())