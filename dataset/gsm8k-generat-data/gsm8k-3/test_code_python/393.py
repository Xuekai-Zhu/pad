def solution():
    """Tony decided he wanted to be an astronaut.  He went to college for 4 years to get a degree in science.  He then went on to get 2 more degrees in other fields for the same period of time.  He also got a graduate degree in physics, which took another 2 years.  How many years in total did Tony go to school to be an astronaut?"""
    # Define the number of years Tony spent in school for each degree
    SCIENCE_DEGREE_YEARS = 4
    OTHER_DEGREES_YEARS = 2
    GRADUATE_DEGREE_YEARS = 2

    # Calculate the total number of years Tony went to school
    total_years = SCIENCE_DEGREE_YEARS + (2 * OTHER_DEGREES_YEARS) + GRADUATE_DEGREE_YEARS

    # Display the total number of years
    result = total_years
    return result

print(solution())