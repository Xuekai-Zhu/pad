def solution():
    """Nathan plays amateur baseball. He played for 3 hours for two weeks, every day. His friend Tobias played for 5 hours every day, but only for one week. How many hours did Nathan and Tobias play in total?"""
    # Calculate Nathan's total playing hours
    nathan_hours = 3 * 7 * 2  

    # Calculate Tobias' total playing hours
    tobias_hours = 5 * 7 * 1  

    # Calculate the total playing hours of Nathan and Tobias
    total_hours = nathan_hours + tobias_hours  

    # Display the total playing hours
    result = total_hours
    return result

print(solution())