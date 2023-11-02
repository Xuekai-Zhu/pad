def solution():
    """Norman High School enrolls an average of 4000 students every year. Butler High School, the neighboring school,
    enrolls an average of 3/4 as many students as Norman High School. How much greater is the average enrollment at
    Norman High School than the enrollment at Butler High School?"""
    norman_enrollment = 4000
    butler_enrollment = (3/4) * norman_enrollment
    difference = norman_enrollment - butler_enrollment
    result = difference
    return result

print(solution())