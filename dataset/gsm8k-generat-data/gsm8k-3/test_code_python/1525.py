def solution():
    """There are three times as many girls as boys in the Biology class. The Physics class has 200 students. If the Biology class has half as many students as the Physics class, how many boys are in the Biology class?"""
    # Calculate the total number of students in the Biology class
    bio_class = 0.5 * 200

    # Calculate the number of girls in the Biology class
    bio_girls = 3/4 * bio_class

    # Calculate the number of boys in the Biology class
    bio_boys = 1/4 * bio_class

    # Display the number of boys in the Biology class
    result = bio_boys
    return result

print(solution())