def solution():
    
    # Define the number of people who entered the restaurant in the morning
    morning_entered = 50

    # Define the number of people who entered the restaurant at the around 10:00
    around_10_00 = morning_entered + 40

    # Define the number of people who entered the restaurant at the 10:00 ordered food
    food_ordered = 2 * around_10_00

    # Define the number of people who entered the restaurant at the 10:00 ordered lunch
    lunch_ordered = 2 * around_10_00

    # Define the number of people who entered the restaurant at the 10:00 evening
    evening_entered = 3 * (food_ordered + lunch_ordered)

    # Calculate the total number of people who entered the restaurant
    total_entered = morning_entered + food_ordered + lunch_ordered + evening_entered

    # Display the total number of people who entered the restaurant
    result = total_entered

print(solution())