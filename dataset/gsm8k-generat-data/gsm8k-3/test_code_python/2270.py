def solution():
    """June’s class has 25 students. 60% are girls and the rest are boys. 40% of the boys like playing basketball and the rest don't. The number of girls who like playing basketball is double the number of boys who don't like to. What percentage of the girls in the class like playing basketball?"""
    # Define the number of students in the class and the percentage of girls and boys
    total_students = 25
    girl_percentage = 0.6
    boy_percentage = 1 - girl_percentage

    # Calculate the number of girls and boys in the class
    num_girls = int(total_students * girl_percentage)
    num_boys = int(total_students * boy_percentage)

    # Calculate the number of boys who like playing basketball and those who don't
    boys_who_like_basketball = int(num_boys * 0.4)
    boys_who_dont_like_basketball = num_boys - boys_who_like_basketball

    # Calculate the number of girls who like playing basketball
    girls_who_like_basketball = boys_who_dont_like_basketball * 2

    # Calculate the percentage of girls who like playing basketball
    percentage_girls_who_like_basketball = (girls_who_like_basketball / num_girls) * 100

    # Display the percentage of girls who like playing basketball
    result = percentage_girls_who_like_basketball
    return result

print(solution())