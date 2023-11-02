def solution():
    """Timmy's parents have a 2 car garage, which has both cars inside it. Also inside is a riding lawnmower, a bicycle for Timmy as well as each of his parents, a tricycle for Timmy's little brother Joey, and a unicycle that Timmy's dad practices riding on. How many wheels in total are in this garage?"""
    
    # Define the number of wheels for each vehicle
    car_wheels = 4
    riding_lawnmower_wheels = 4
    bicycle_wheels = 2
    tricycle_wheels = 3
    unicycle_wheels = 1
    
    # Calculate the total number of wheels in the garage
    total_wheels = (2 * car_wheels) + riding_lawnmower_wheels + (3 * bicycle_wheels) + tricycle_wheels + unicycle_wheels
    
    # Return the result
    result = total_wheels
    return result

print(solution())