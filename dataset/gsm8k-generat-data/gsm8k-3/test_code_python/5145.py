def solution():
    """A class is 40% boys. The rest are girls. Every boy in class gets an 80% on the math test. Every girl gets a 90%. What is the class average on the test?"""
    # Define the percentage of boys in the class and the test scores for boys and girls
    BOY_PERCENTAGE = 0.4
    BOY_SCORE = 0.8
    GIRL_SCORE = 0.9

    # Calculate the percentage of girls in the class
    girl_percentage = 1 - BOY_PERCENTAGE

    # Calculate the class average
    class_avg = (BOY_PERCENTAGE * BOY_SCORE) + (girl_percentage * GIRL_SCORE)

    # Display the class average
    result = class_avg
    return result

print(solution())