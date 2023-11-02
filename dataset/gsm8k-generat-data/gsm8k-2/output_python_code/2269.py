def solution():
    """June’s class has 25 students. 60% are girls and the rest are boys. 40% of the boys like playing basketball and the rest don't. The number of girls who like playing basketball is double the number of boys who don't like to. What percentage of the girls in the class like playing basketball?"""
    total_students = 25
    girls_percent = 0.6
    boys_percent = 1 - girls_percent
    boys_who_play_basketball_percent = 0.4
    boys_who_dont_play_basketball_percent = 1 - boys_who_play_basketball_percent
    boys_who_dont_play_basketball = boys_who_dont_play_basketball_percent * boys_percent * total_students
    girls_who_play_basketball = 2 * boys_who_dont_play_basketball
    girls_total = girls_percent * total_students
    girls_who_play_basketball_percent = (girls_who_play_basketball / girls_total) * 100
    result = girls_who_play_basketball_percent
    return result

print(solution())