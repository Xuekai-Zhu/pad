def solution():
    """Timmy's parents have a 2 car garage, which has both cars inside it. Also inside is a riding lawnmower, a bicycle for Timmy as well as each of his parents, a tricycle for Timmy's little brother Joey, and a unicycle that Timmy's dad practices riding on. How many wheels in total are in this garage?"""
    car_wheels = 4 * 2
    lawnmower_wheels = 4
    timmy_bike_wheels = 2
    parent_bike_wheels = 2 * 2
    joey_trike_wheels = 3
    dad_unicycle_wheels = 1
    total_wheels = car_wheels + lawnmower_wheels + timmy_bike_wheels + parent_bike_wheels + joey_trike_wheels + dad_unicycle_wheels
    result = total_wheels
    return result

print(solution())