def solution():
    minutes_per_side = 4
    burgers_per_grill = 5
    total_guests = 30
    guests_wanting_two_burgers = total_guests / 2
    guests_wanting_one_burger = total_guests / 2
    total_burgers = guests_wanting_two_burgers + guests_wanting_one_burger
    minutes_to_cook = total_burgers * minutes_per_side
    result = minutes_to_cook
    return result

print(solution())