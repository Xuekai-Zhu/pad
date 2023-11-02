def solution():
    """Gumball was counting his water intake for the previous week. He checked his list and saw that he had drank 60 liters of water for the week. He drank nine liters of water on Monday, Thursday and Saturday and 8 liters of water on Tuesday, Friday and Sunday. Unfortunately, no data was input on Wednesday. How many liters of water did he drink on Wednesday?"""
    # Define the total amount of water drank for the week
    total_water = 60

    # Define the amount of water drank on each day
    monday_water = 9
    tuesday_water = 8
    wednesday_water = 0 # no data input
    thursday_water = 9
    friday_water = 8
    saturday_water = 9
    sunday_water = 8

    # Calculate the amount of water drank on Wednesday
    wednesday_water = total_water - (monday_water*3 + tuesday_water*2 + thursday_water*2 + friday_water*2 + saturday_water*2 + sunday_water*2)

    # Display the amount of water drank on Wednesday
    result = wednesday_water
    return result

print(solution())