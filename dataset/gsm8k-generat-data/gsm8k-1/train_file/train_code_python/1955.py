def solution():
    """It takes Matt 2 minutes per problem to do his math homework with a calculator and 5 minutes per problem without a calculator. If Matt's assignment has 20 problems, how much time will using a calculator save?"""
    num_problems = 20
    time_with_calc = num_problems * 2
    time_without_calc = num_problems * 5
    time_saved = time_without_calc - time_with_calc
    result = time_saved
    return result

print(solution())