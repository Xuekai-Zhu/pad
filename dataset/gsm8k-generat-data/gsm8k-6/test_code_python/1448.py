def solution():
    # Calculate the total number of notebooks in the classroom
    half_students = 28//2 
    half_notebooks_5 = half_students * 5 
    half_notebooks_3 = half_students * 3 
    total_notebooks = half_notebooks_5 + half_notebooks_3 
    result = total_notebooks
    return result

print(solution())