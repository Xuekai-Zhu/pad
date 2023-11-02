def solution():
    # Define the facts about Queen Elizabeth I and Reza Shah
    queen_elizabeth_nationality = "English"
    reza_shah_nationality = "Mazanderani"
    mazanderani_origin = "Iran"
    distance_england_iran = 4000
    # Check if it is possible for Reza Shah to be related to Queen Elizabeth I
    if reza_shah_nationality == queen_elizabeth_nationality \
        or mazanderani_origin == queen_elizabeth_nationality \
        or distance_england_iran < 5000:
        result = "possibly"
    else:
        result = "unlikely"
    return result

print(solution())