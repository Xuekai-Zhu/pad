def solution():
    # Define the percentage of boys and girls in the class
    boys_percentage = 0.4
    girls_percentage = 1 - boys_percentage

    # Define the test scores for boys and girls
    boys_score = 0.8
    girls_score = 0.9

    # Calculate the weighted average of the class
    class_average = boys_percentage * boys_score + girls_percentage * girls_score
    result = class_average
    return result

print(solution())