def solution():
    """Mrs. Gable’s third grade class is on a field trip to the beach. For lunch, Mrs. Gable brought 20 lunches for the 20 students in her class. She included a pack of animal crackers in each lunch bag for dessert. Each pack of animal crackers contained 10 animal crackers. If 2 students did not eat their animal crackers, how many animal crackers were eaten in total among Mrs. Gable’s students?"""
    # Define the number of lunches and animal crackers per lunch
    num_lunches = 20
    crackers_per_lunch = 10

    # Calculate the total number of animal crackers
    total_crackers = num_lunches * crackers_per_lunch

    # Subtract the number of uneaten animal crackers
    total_crackers -= 2

    # Calculate the number of eaten animal crackers
    eaten_crackers = total_crackers - 2

    result = eaten_crackers
    return result

print(solution())