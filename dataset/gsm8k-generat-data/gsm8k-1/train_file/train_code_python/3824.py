def solution():
    """There were 37 jellybeans in a jar. Pat removed 15 of them. Pat then added 5 of the removed jellybeans back in, and then removed 4 more. How many jellybeans are now in the jar?"""
    initial_jellybeans = 37
    jellybeans_removed = 15
    jellybeans_added = 5
    jellybeans_removed_again = 4
    total_jellybeans = initial_jellybeans - jellybeans_removed + jellybeans_added - jellybeans_removed_again
    result = total_jellybeans
    return result

print(solution())