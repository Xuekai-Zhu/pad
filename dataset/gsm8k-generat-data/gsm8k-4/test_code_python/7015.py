def solution():
    """Cassidy collects movie posters from newly released sci-fi movies. After this summer, she will have six more posters in her collection, making it double the size it was two years ago when she had 14 posters. How many posters does she have now?"""
    # Define the number of posters Cassidy had two years ago
    posters_two_years_ago = 14

    # Define the number of posters Cassidy will have after this summer
    posters_after_summer = posters_two_years_ago * 2 + 6

    # Calculate the current number of posters Cassidy has
    current_posters = posters_after_summer - 6

    # return the result
    result = current_posters
    return result

print(solution())