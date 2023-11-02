def solution():
    """Matt needs to buy new plates for his home.  He only wants to do dishes once a week.  Three days a week it is only him and his son eating and they use 1 plate each.  On the remainder of the days, his parents join them and everyone uses 2 plates that day.  How many plates does he need to buy?"""
    # Define the number of plates used by Matt and his son on 3 days
    plates_matt_son = 1
    days_matt_son = 3

    # Define the number of plates used by everyone on 4 days
    plates_everyone = 2
    days_everyone = 4

    # Calculate the total number of plates needed per week
    total_plates = (plates_matt_son * days_matt_son) + (plates_everyone * days_everyone)

    # Multiply by 7 to get the total plates needed for one week
    total_plates *= 7

    # Display the total number of plates needed
    result = total_plates
    return result

print(solution())