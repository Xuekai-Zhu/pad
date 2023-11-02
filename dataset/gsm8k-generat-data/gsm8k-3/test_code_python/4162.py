def solution():
    """Jerry's breakfast includes 6 pancakes with 120 calories each, two strips of bacon with 100 calories each, and a bowl of cereal with 200 calories. How many calories is his breakfast total?"""
    # Define the number of pancakes and the calories per pancake
    num_pancakes = 6
    pancake_cal = 120

    # Define the number of strips of bacon and the calories per strip
    num_bacon = 2
    bacon_cal = 100

    # Define the number of calories in the bowl of cereal
    cereal_cal = 200

    # Calculate the total number of calories in Jerry's breakfast
    total_calories = (num_pancakes * pancake_cal) + (num_bacon * bacon_cal) + cereal_cal

    # Display the total number of calories
    result = total_calories
    return result

print(solution())