def solution():
    """At the Johnson family reunion, there were 45 children and one third as many adults. One third of the adults wore blue. How many adults did not wear blue?"""
    # Calculate the number of adults
    adults = 45 * 3

    # Calculate the number of adults who wore blue
    blue_adults = adults // 3

    # Calculate the number of adults who did not wear blue
    non_blue_adults = adults - blue_adults

    # Display the number of adults who did not wear blue
    result = non_blue_adults
    return result

print(solution())