def solution():
    # Define the number of students who attended school
    num_students = 24 - 2

    # Calculate the total number of jellybeans eaten
    total_jellybeans_eaten = num_students * 3

    # Calculate the number of jellybeans still in the jar
    jellybeans_left = 100 - total_jellybeans_eaten
    result = jellybeans_left
    return result

print(solution())