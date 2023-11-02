def solution():
    """There are 180 students in ninth grade. 1/4 of them bombed their finals because they were going through difficult breakups. 1/3rd of the rest didn't show up to take the test, and another 20 got less than a D. How many students passed their finals?"""
    # Calculate the number of students who bombed their finals due to difficult breakups
    bombed = 180 // 4

    # Calculate the number of students who didn't show up for the test
    didnt_show_up = (180 - bombed) // 3

    # Calculate the number of students who got less than a D
    less_than_d = 20

    # Calculate the number of students who passed their finals
    passed_finals = 180 - bombed - didnt_show_up - less_than_d

    # Display the number of students who passed their finals
    result = passed_finals
    return result

print(solution())