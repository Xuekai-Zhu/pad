def solution():
    
    # Define the number of males and females
    num_males = 8
    num_females = 6

    # Calculate the number of dumplings eaten by each male and each female
    male_dumplings = num_females * 3
    female_dumplings = num_males * 3

    # Calculate the total number of dumplings eaten
    total_dumplings = male_dumplings + female_dumplings

    # Display the total number of dumplings
    result = total_dumplings
    return result

print(solution())