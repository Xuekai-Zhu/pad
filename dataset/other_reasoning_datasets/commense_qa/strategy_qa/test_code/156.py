def solution():
    # Define the definition of Myocardial infarction and stroke
    myocardial_infarction_problem = "problem in the heart"
    stroke_problem = "similar problem in the brain"
    # Check if Myocardial infarction is related to a brain problem
    if myocardial_infarction_problem != stroke_problem:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())