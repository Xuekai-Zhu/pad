def solution():
    """Max likes to collect model trains.  He asks for one for every birthday of his, and asks for two each Christmas.  Max always gets the gifts he asks for, and asks for these same gifts every year for 5 years.  At the end of the 5 years, his parents give him double the number of trains he already has.  How many trains does Max have now?"""
    # Define the number of trains Max starts with
    starting_trains = 0

    # Calculate the number of trains Max receives each year
    birthday_trains = 1
    christmas_trains = 2
    total_yearly_trains = birthday_trains + christmas_trains

    # Calculate the total number of trains Max receives over 5 years
    total_trains_received = total_yearly_trains * 5

    # Calculate the total number of trains Max has at the end of 5 years
    total_trains = starting_trains + total_trains_received

    # Calculate the number of trains Max receives as a gift from his parents
    parents_gift = total_trains * 2

    # Calculate the final total number of trains Max has
    final_total = total_trains + parents_gift

    # Display the final total number of trains Max has
    result = final_total
    return result

print(solution())