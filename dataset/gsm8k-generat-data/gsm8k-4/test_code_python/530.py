def solution():
    """Pat is having a picnic with her family. She has 42 cookies. She also has 63 pieces of candy and 21 brownies. There are 7 people in her family. If each person gets the same number of each dessert, how much will each person get?"""
    # Define the total number of each dessert
    total_cookies = 42
    total_candy = 63
    total_brownies = 21

    # Define the number of people in the family
    num_people = 7

    # Calculate the total number of desserts
    total_desserts = total_cookies + total_candy + total_brownies

    # Calculate the number of each dessert each person will get
    num_each_dessert = total_desserts / (num_people * 3)

    result = num_each_dessert
    return result

print(solution())