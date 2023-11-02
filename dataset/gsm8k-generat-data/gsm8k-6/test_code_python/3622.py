def solution():
    # Calculate the number of pencils Clare bought
    pencils_Clare = 18 / 2  

    # Calculate the number of pencils Jeanine gave to Abby
    pencils_Jeanine = 18
    pencils_Abby = pencils_Jeanine / 3

    # Calculate how many pencils Jeanine has now
    pencils_Jeanine_now = pencils_Jeanine - pencils_Abby

    # Calculate the difference between Jeanine and Clare's number of pencils
    difference = pencils_Jeanine_now - pencils_Clare
    result = difference
    return result

print(solution())