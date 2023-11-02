def solution():
    """Tom eats a pound of carrots and twice as much broccoli.  If carrots have 51 calories per pound and broccoli has 1/3 that many calories, how many calories did he eat in total?"""
    # Define the number of pounds of carrots and broccoli
    carrot_pounds = 1
    broccoli_pounds = 2

    # Define the number of calories per pound for each vegetable
    carrot_calories = 51
    broccoli_calories = carrot_calories / 3

    # Calculate the total number of calories Tom ate
    total_calories = (carrot_pounds * carrot_calories) + (broccoli_pounds * broccoli_calories)

    # Display the total number of calories
    result = total_calories
    return result

print(solution())