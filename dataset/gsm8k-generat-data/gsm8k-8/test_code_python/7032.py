def solution():
    # Define the variables
    dozens_of_donuts = 2.5
    donuts_per_dozen = 12
    total_donuts = dozens_of_donuts * donuts_per_dozen
    percent_eaten = 0.1
    donuts_eaten = total_donuts * percent_eaten
    donuts_for_afternoon_snack = 4

    # Calculate the number of donuts left for Chris' coworkers
    remaining_donuts = total_donuts - donuts_eaten - donuts_for_afternoon_snack
    result = remaining_donuts
    return result

print(solution())