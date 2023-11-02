def solution():
    """June’s class has 25 students. 60% are girls and the rest are boys. 40% of the boys like playing basketball and the rest don't. 
    The number of girls who like playing basketball is double the number of boys who don't like to. 
    What percentage of the girls in the class like playing basketball?"""
    total_students = 25
    girls_percent = 60
    boys_percent = 100 - girls_percent
    girls = total_students * (girls_percent / 100)
    boys = total_students - girls
    boys_basketball = boys * 0.4
    girls_basketball = 2 * (boys - boys_basketball)
    total_basketball = boys_basketball + girls_basketball
    percent_girls_basketball = (girls_basketball / girls) * 100
    result = percent_girls_basketball
    return result

print(solution())