def solution():
    """Pat is having a picnic with her family. She has 42 cookies. She also has 63 pieces of candy and 21 brownies. There are 7 people in her family. If each person gets the same number of each dessert, how much will each person get?"""
    # Define the number of desserts Pat has
    num_cookies = 42
    num_candy = 63
    num_brownies = 21

    # Define the number of people in Pat's family
    num_people = 7

    # Calculate the number of each dessert each person will get
    num_each = (num_cookies + num_candy + num_brownies) // (3 * num_people)

    # Display how much each person will get
    result = num_each
    return result

print(solution())