def solution():
    # Define the number of apples Sarah started with
    starting_apples = 25

    # Calculate the number of apples she gave to teachers
    teacher_apples = starting_apples - 3  # She ate one on the way home
    # Calculate the number of friends who received an apple
    friend_apples = 5
    # Calculate the total number of apples given away
    total_apples_given = teacher_apples + friend_apples
    result = total_apples_given
    return result

print(solution())