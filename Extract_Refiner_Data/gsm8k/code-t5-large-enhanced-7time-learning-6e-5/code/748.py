def solution():
    
    # Define the number of roommates and the monthly electricity bill
    num_roommates = 4
    monthly_bill = 100

    # Calculate the total electricity bill per year
    total_bill = num_roommates * monthly_bill * 12

    # Calculate the cost per roommate per year
    cost_per_roommate = total_bill / num_roommates

    # Display the cost per roommate per year
    result = cost_per_roommate
    return result

print(solution())