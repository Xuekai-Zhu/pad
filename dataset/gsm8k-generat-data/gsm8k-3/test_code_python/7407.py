def solution():
    """The school store had a sale on pencils. Ten students bought pencils. The first two students bought 2 pencils each. The next six students bought three pencils each and the last two students only bought one pencil each. How many pencils were sold?"""
    # Define the number of pencils bought by each group of students
    first_two = 2 * 2
    next_six = 6 * 3
    last_two = 2 * 1

    # Calculate the total number of pencils sold
    total_pencils = first_two + next_six + last_two

    # Display the total number of pencils sold
    result = total_pencils
    return result

print(solution())