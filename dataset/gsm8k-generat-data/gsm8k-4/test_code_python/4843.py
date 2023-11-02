def solution():
    """Josh has soccer practice on Monday, Wednesday, and Friday from 3:00 p.m. to 5:00 p.m. He has band practice on Tuesday and Thursday from 3:30 p.m. to 5:00 p.m. From Monday to Friday, how many hours does Josh spend on extracurricular activities?"""
    # Define the duration of soccer practice and band practice
    soccer_duration = 2
    band_duration = 1.5

    # Calculate the total duration of extracurricular activities on weekdays
    total_duration = (soccer_duration * 3) + (band_duration * 2)

    # return the result
    result = total_duration
    return result

print(solution())