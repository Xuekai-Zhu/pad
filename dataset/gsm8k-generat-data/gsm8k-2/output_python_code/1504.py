def solution():
    """Mary had 6 lambs and 2 of the lambs had 2 babies each. She traded 3 lambs for one goat. One 
    morning, she woke up and found an extra 7 lambs in the field. How many lambs does Mary have?"""

    # initial number of lambs
    lambs = 6 

    # adding lambs from offspring
    lambs += 2*2 

    # trading 3 lambs for a goat
    lambs -= 3 

    # finding extra 7 lambs in the field
    lambs += 7 

    result = lambs
    return result

print(solution())