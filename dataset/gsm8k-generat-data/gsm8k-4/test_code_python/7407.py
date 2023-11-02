def solution():
    """The school store had a sale on pencils. Ten students bought pencils. The first two students bought 2 pencils each. The next six students bought three pencils each and the last two students only bought one pencil each. How many pencils were sold?"""
    # Calculate the number of pencils bought by the first two students
    pencils_first_two = 2 * 2

    # Calculate the number of pencils bought by the next six students
    pencils_six_students = 6 * 3

    # Calculate the number of pencils bought by the last two students
    pencils_last_two = 2 * 1

    # Calculate the total number of pencils sold
    total_pencils = pencils_first_two + pencils_six_students + pencils_last_two

    result = total_pencils
    return result

print(solution())