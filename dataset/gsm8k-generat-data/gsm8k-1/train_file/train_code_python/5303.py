def solution():
    """Gumball was counting his water intake for the previous week. He checked his list and saw that he had drank 60 liters of water for the week. He drank nine liters of water on Monday, Thursday and Saturday and 8 liters of water on Tuesday, Friday and Sunday. Unfortunately, no data was input on Wednesday. How many liters of water did he drink on Wednesday?"""
    total_water = 60
    water_on_other_days = 9*3 + 8*3 # 9 liters on Mon, Thurs, Sat and 8 liters on Tues, Fri, Sun.
    water_on_wednesday = total_water - water_on_other_days # Subtracting to find out the liters of water drank on Wednesday.
    result = water_on_wednesday
    return result

print(solution())