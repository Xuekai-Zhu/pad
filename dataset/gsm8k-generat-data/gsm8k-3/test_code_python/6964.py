def solution():
    """James binges on Cheezits and eats 3 bags that are 2 ounces each.  There are 150 calories in an ounce of Cheezits.  He then goes for a 40-minute run and burns 12 calories per minute.  How many excess calories did he eat?"""
    # Define the number of bags of Cheezits and the number of ounces per bag
    num_bags = 3
    ounces_per_bag = 2

    # Calculate the total number of ounces of Cheezits eaten
    total_ounces = num_bags * ounces_per_bag

    # Calculate the total number of calories consumed
    calories_consumed = total_ounces * 150

    # Calculate the number of calories burned during the run
    calories_burned = 40 * 12

    # Calculate the excess calories consumed
    excess_calories = calories_consumed - calories_burned

    # Display the excess calories consumed
    result = excess_calories
    return result

print(solution())