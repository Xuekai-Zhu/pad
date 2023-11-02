def solution():
    """Tony decided he wanted to be an astronaut. He went to college for 4 years to get a degree in science. He then went on to get 2 more degrees in other fields for the same period of time. He also got a graduate degree in physics, which took another 2 years. How many years in total did Tony go to school to be an astronaut?"""
    # Define the number of years Tony spent in school for each degree
    science_degree_years = 4
    other_degrees_years = 2
    physics_degree_years = 2

    # Calculate the total number of years Tony spent in school
    total_years = science_degree_years + (2 * other_degrees_years) + physics_degree_years

    result = total_years
    return result

print(solution())