def solution():
    """Tony decided he wanted to be an astronaut. He went to college for 4 years to get a degree in science. He then went on to get 2 more degrees in other fields for the same period of time. He also got a graduate degree in physics, which took another 2 years. How many years in total did Tony go to school to be an astronaut?"""
    years_for_college_degree = 4
    total_years_for_other_degrees = 2 * 4
    years_for_graduate_degree = 2
    total_years = years_for_college_degree + total_years_for_other_degrees + years_for_graduate_degree
    result = total_years
    return result

print(solution())