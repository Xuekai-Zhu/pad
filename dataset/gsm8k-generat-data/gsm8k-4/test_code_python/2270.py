def solution():
    """June’s class has 25 students. 60% are girls and the rest are boys. 40% of the boys like playing basketball and the rest don't. The number of girls who like playing basketball is double the number of boys who don't like to. What percentage of the girls in the class like playing basketball?"""
    # Define the total number of students and the percentage of girls
    total_students = 25
    girls_percentage = 0.6

    # Calculate the number of girls and boys
    girls = int(total_students * girls_percentage)
    boys = total_students - girls

    # Calculate the number of boys who like playing basketball and those who don't
    boys_play_basketball = int(boys * 0.4)
    boys_dont_play_basketball = boys - boys_play_basketball

    # Calculate the number of girls who like playing basketball
    girls_play_basketball = boys_dont_play_basketball * 2

    # Calculate the percentage of girls who like playing basketball
    girls_play_basketball_percentage = (girls_play_basketball / girls) * 100

    result = girls_play_basketball_percentage
    return result

print(solution())