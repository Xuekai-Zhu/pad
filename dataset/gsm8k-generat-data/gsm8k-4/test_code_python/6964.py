def solution():
    """James binges on Cheezits and eats 3 bags that are 2 ounces each. There are 150 calories in an ounce of Cheezits. He then goes for a 40-minute run and burns 12 calories per minute. How many excess calories did he eat?"""
    # Define the number of bags and the weight per bag
    num_bags = 3
    bag_weight = 2  # in ounces

    # Calculate the total weight of Cheezits eaten
    total_weight = num_bags * bag_weight  # in ounces

    # Calculate the total number of calories consumed
    calories_consumed = total_weight * 150

    # Calculate the number of calories burned during the run
    calories_burned = 40 * 12

    # Calculate the excess calories consumed
    excess_calories = calories_consumed - calories_burned

    # return the result
    result = excess_calories
    return result

print(solution())