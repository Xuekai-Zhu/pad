def solution():
    """Timmy's parents have a 2 car garage, which has both cars inside it. Also inside is a riding lawnmower, a bicycle for Timmy as well as each of his parents, a tricycle for Timmy's little brother Joey, and a unicycle that Timmy's dad practices riding on. How many wheels in total are in this garage?"""
    num_wheels_per_car = 4
    num_wheels_per_timmys_bike = 2
    num_wheels_per_parents_bike = 2
    num_wheels_per_joeys_tricycle = 3
    num_wheels_per_dads_unicycle = 1
    num_wheels = (2 * num_wheels_per_car) + num_wheels_per_timmys_bike + (2 * num_wheels_per_parents_bike) + num_wheels_per_joeys_tricycle + num_wheels_per_dads_unicycle
    result = num_wheels
    return result

print(solution())