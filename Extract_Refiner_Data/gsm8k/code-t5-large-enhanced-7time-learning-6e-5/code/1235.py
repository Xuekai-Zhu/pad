def solution():
    
    # Define the number of classrooms and the time it takes to clean each classroom
    NUM_CLASSROOMS = 80
    TIME_PER_CLASSROOM = 15 # in minutes

    # Define the number of days the custodian has to clean the school
    NUM_DAYS = 5

    # Calculate the total time spent cleaning classrooms
    total_time = NUM_DAYS * TIME_PER_CLASSROOM

    # Calculate the average time spent cleaning classrooms per day
    avg_time_per_day = total_time / NUM_DAYS

    # Calculate the percentage of their day spent cleaning classrooms
    percentage_spent_per_day = (avg_time_per_day / NUM_DAYS) * 100

    # Display the percentage spent cleaning classrooms per day
    result = percentage_spent_per_day
    return result

print(solution())