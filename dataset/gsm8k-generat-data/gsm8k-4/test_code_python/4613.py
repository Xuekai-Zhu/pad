def solution():
    """A class of 30 high school students is preparing for a field trip. If each student contributes $2 every Friday for their trip, how many dollars will they have in 2 months?"""
    # Define the number of students and the contribution amount
    num_students = 30
    contribution = 2

    # Calculate the number of Fridays in 2 months
    num_fridays = 8

    # Calculate the total amount of money collected
    total_money = num_students * contribution * num_fridays

    # Return the result
    result = total_money
    return result

print(solution())