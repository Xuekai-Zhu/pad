def solution():
    """Jared is trying to increase his typing speed. He starts with 47 words per minute (WPM). 
    After some lessons the next time he tests his typing speed it has increased to 52 WPM. 
    If he continues to increase his typing speed once more by 5 words, what will be the average of the three measurements?"""
    initial_wpm = 47
    second_wpm = 52
    third_wpm = second_wpm + 5
    average_wpm = (initial_wpm + second_wpm + third_wpm) / 3
    result = average_wpm
    return result

print(solution())