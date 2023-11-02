def solution():
    """On Monday, Matt worked for 450 minutes in his office. On Tuesday, he worked half the number of minutes he worked on Monday. On Wednesday, he worked for 300 minutes. How many more minutes did he work on Wednesday than on Tuesday?"""
    # Calculate the number of minutes Matt worked on Tuesday
    tuesday_minutes = 450 / 2

    # Calculate the difference between the number of minutes Matt worked on Wednesday and Tuesday
    wednesday_tuesday_diff = 300 - tuesday_minutes

    result = wednesday_tuesday_diff
    return result

print(solution())