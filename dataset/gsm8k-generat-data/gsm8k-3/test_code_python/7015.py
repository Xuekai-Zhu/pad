def solution():
    """Cassidy collects movie posters from newly released sci-fi movies. After this summer, she will have six more posters in her collection, making it double the size it was two years ago when she had 14 posters. How many posters does she have now?"""
    # Define the number of posters Cassidy had two years ago
    posters_2_years_ago = 14

    # Define the number of additional posters Cassidy will have after this summer
    additional_posters = 6

    # Calculate the current number of posters Cassidy has
    current_posters = (posters_2_years_ago * 2) + additional_posters

    # Display the current number of posters Cassidy has
    result = current_posters
    return result

print(solution())