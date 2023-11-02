def solution():
    """A class is 40% boys. The rest are girls. Every boy in class gets an 80% on the math test. Every girl gets a 90%. What is the class average on the test?"""
    # Define the percentage of boys and girls
    boy_percentage = 0.4
    girl_percentage = 1 - boy_percentage

    # Define the boys' and girls' test scores
    boy_score = 0.8
    girl_score = 0.9

    # Calculate the class average on the test
    class_average = boy_percentage * boy_score + girl_percentage * girl_score

    result = class_average
    return result

print(solution())