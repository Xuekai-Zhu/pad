def solution():
    
    # Define the number of people who entered the restaurant in the morning
    morning_eaten = 50

    # Calculate the number of people who ordered food
    food_eaten = morning_eaten + 40

    # Calculate the number of people who ordered lunch
    lunch_eaten = 2 * food_eaten

    # Calculate the total number of people who entered the restaurant
    total_entered = morning_eaten + food_eaten + lunch_eaten

    # Calculate the additional number of people who entered the restaurant
    additional_people = 3 * total_entered

    # Calculate the total number of people who entered the restaurant
    total_entered = total_entered + additional_people

    # Display the total number of people who entered the restaurant
    result = total_entered
    return result

print(solution())