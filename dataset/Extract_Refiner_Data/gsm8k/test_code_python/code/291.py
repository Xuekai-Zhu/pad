def solution():
    
    # Define the number of activities on the first day
    pushup_1 = 100
    squat_1 = 50
    dumbbell_press_1 = 20

    # Define the number of activities on the second day
    pushup_2 = pushup_1 + 20
    squat_2 = squat_1 - 10
    dumbbell_press_2 = dumbbell_press_1 * 2

    # Calculate the total number of activities done in the two days
    total_pushup_count = pushup_1 + pushup_2
    total_squat_count = squat_1 + squat_2
    total_dumbbell_press_count = dumbbell_press_1 + dumbbell_press_2
    total_count = total_pushup_count + total_squat_count + total_dumbbell_press_count

    # Display the total count
    result = total_count
    return result

print(solution())