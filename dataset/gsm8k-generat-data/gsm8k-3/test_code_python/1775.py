def solution():
    """One student on a field trip counted 12 squirrels. Another counted a third more squirrels than the first student. How many squirrels did both students count combined?"""
    # Define the number of squirrels counted by the first student
    squirrels_1 = 12

    # Define the number of squirrels counted by the second student (a third more than the first)
    squirrels_2 = squirrels_1 + (squirrels_1 * (1/3))

    # Calculate the total number of squirrels counted
    total_squirrels = squirrels_1 + squirrels_2

    # Display the total number of squirrels counted
    result = total_squirrels
    return result

print(solution())