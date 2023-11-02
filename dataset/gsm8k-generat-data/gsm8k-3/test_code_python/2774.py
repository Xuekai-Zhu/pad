def solution():
    """Officer Hopps has to give out 200 tickets in May. The first 15 days he averages 8 tickets a day. How many does he have to average each day for the rest of the month to reach his required goal?"""
    # Define the total number of tickets required
    total_tickets = 200

    # Define the number of days in May
    days_in_may = 31

    # Define the number of tickets given out in the first 15 days
    tickets_given_first_15_days = 8 * 15

    # Calculate the number of tickets Officer Hopps still has to give out
    tickets_left = total_tickets - tickets_given_first_15_days

    # Calculate the number of days left in May
    days_left = days_in_may - 15

    # Calculate the average number of tickets Officer Hopps needs to give out each day for the rest of the month
    tickets_per_day = tickets_left / days_left

    # Display the average number of tickets Officer Hopps needs to give out each day for the rest of the month
    result = tickets_per_day
    return result

print(solution())