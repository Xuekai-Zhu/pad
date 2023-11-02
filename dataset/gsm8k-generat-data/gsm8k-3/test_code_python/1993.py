def solution():
    """Georgia is sick and coughs 5 times a minute. Her brother Robert is also sick but he coughs twice as much as her. After 20 minutes, how many times have they coughed?"""
    
    # Calculate the number of times Georgia coughs in 20 minutes
    georgia_coughs = 5 * 20
    
    # Calculate the number of times Robert coughs in 20 minutes
    robert_coughs = 2 * georgia_coughs
    
    # Calculate the total number of coughs in 20 minutes
    total_coughs = georgia_coughs + robert_coughs
    
    # Display the total number of coughs in 20 minutes
    result = total_coughs
    return result

print(solution())