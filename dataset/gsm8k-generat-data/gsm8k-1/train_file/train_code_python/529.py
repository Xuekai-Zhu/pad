def solution():
    """Pat is having a picnic with her family. She has 42 cookies. She also has 63 pieces of candy and 21 brownies. There are 7 people in her family. If each person gets the same number of each dessert, how much will each person get?"""
    total_cookies = 42
    total_candy = 63
    total_brownies = 21
    total_people = 7

    # Calculate total number of desserts
    total_desserts = total_cookies + total_candy + total_brownies

    # Calculate number of each dessert per person
    desserts_per_person = total_desserts / total_people

    result = desserts_per_person
    return result

print(solution())