def solution():
    """Georgia is sick and coughs 5 times a minute. Her brother Robert is also sick but he coughs twice as much as her. After 20 minutes, how many times have they coughed?"""
    # Define the number of coughs per minute for Georgia and Robert
    georgia_coughs_per_minute = 5
    robert_coughs_per_minute = georgia_coughs_per_minute * 2

    # Calculate the total number of coughs for Georgia and Robert after 20 minutes
    total_georgia_coughs = georgia_coughs_per_minute * 20
    total_robert_coughs = robert_coughs_per_minute * 20

    # Calculate the total number of coughs for both of them together
    total_coughs = total_georgia_coughs + total_robert_coughs

    # return the result
    result = total_coughs
    return result

print(solution())