def solution():
    """For a class fundraiser, 30 students were asked to bring in 12 brownies each.  20 students were asked to bring in 24 cookies each and 15 students were asked to bring in 12 donuts each.  If they sell everything for $2.00 each, how much money will they raise?"""
    # Define the number of items each student brings in
    BROWNIES_PER_STUDENT = 12
    COOKIES_PER_STUDENT = 24
    DONUTS_PER_STUDENT = 12

    # Define the number of students for each pastry type
    NUM_BROWNIE_STUDENTS = 30
    NUM_COOKIE_STUDENTS = 20
    NUM_DONUT_STUDENTS = 15

    # Calculate the total number of items
    total_brownies = BROWNIES_PER_STUDENT * NUM_BROWNIE_STUDENTS
    total_cookies = COOKIES_PER_STUDENT * NUM_COOKIE_STUDENTS
    total_donuts = DONUTS_PER_STUDENT * NUM_DONUT_STUDENTS
    total_items = total_brownies + total_cookies + total_donuts

    # Calculate the total amount of money raised
    total_money = total_items * 2

    # Display the total amount of money raised
    result = total_money
    return result

print(solution())