def solution():
    """The kids in Ms. Swanson's class have an average of 5 zits each. The kids in Mr. Jones' class have an average of six zits each. If there are 25 kids in Ms. Swanson's class and 32 in Mr. Jones' class, how many more zits are there in Mr. Jones' class than in Ms. Swanson's?"""
    swanson_average = 5
    jones_average = 6
    swanson_students = 25
    jones_students = 32
    swanson_zits = swanson_average * swanson_students
    jones_zits = jones_average * jones_students
    difference = jones_zits - swanson_zits
    result = difference
    return result

print(solution())