def solution():
    """Chris is way behind on his math homework. He has 100 math problems to complete in total. He completes 12 problems on Monday night.
    On Tuesday, he completes 3 times as many problems as he did on Monday. On Wednesday, he completes one-quarter of the remaining math problems.
    How many math problems does he have left to complete on Thursday?"""
    
    total_problems = 100
    monday_problems = 12
    tuesday_problems = monday_problems * 3
    remaining_problems = total_problems - monday_problems - tuesday_problems
    wednesday_problems = remaining_problems // 4
    thursday_problems = remaining_problems - wednesday_problems
    
    return thursday_problems

print(solution())