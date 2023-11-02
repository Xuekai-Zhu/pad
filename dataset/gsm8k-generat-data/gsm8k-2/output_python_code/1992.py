def solution():
    """Georgia is sick and coughs 5 times a minute. Her brother Robert is also sick but he coughs twice as much as her. After 20 minutes, how many times have they coughed?"""
    georgia_cough_rate = 5
    robert_cough_rate = 2 * georgia_cough_rate
    total_coughs = (georgia_cough_rate + robert_cough_rate) * 20
    result = total_coughs
    return result

print(solution())