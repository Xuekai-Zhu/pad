def solution():
    """At the Johnson family reunion, there were 45 children and one third as many adults. One third of the adults wore blue. How many adults did not wear blue?"""
    # Calculate the number of children and adults
    total_people = 45 + (45 * 3)
    adults = total_people - 45

    # Calculate the number of adults who wore blue
    blue_adults = adults // 3

    # Calculate the number of adults who did not wear blue
    nonblue_adults = adults - blue_adults

    # Return the result
    result = nonblue_adults
    return result

print(solution())