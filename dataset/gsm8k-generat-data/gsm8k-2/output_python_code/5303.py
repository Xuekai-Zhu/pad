def solution():
    """Gumball was counting his water intake for the previous week. He checked his list and saw that he had drank 60 liters of water for the week. He drank nine liters of water on Monday, Thursday and Saturday and 8 liters of water on Tuesday, Friday and Sunday. Unfortunately, no data was input on Wednesday. How many liters of water did he drink on Wednesday?"""
    liters_per_day = 8.57
    total_days = 7
    total_liters = 60
    liters_on_mon_thur_sat = 9
    liters_on_tue_fri_sun = 8
    liters_on_other_days = total_liters - (liters_on_mon_thur_sat*3) - (liters_on_tue_fri_sun*3)
    liters_on_wednesday = total_liters - liters_on_other_days - (liters_on_tue_fri_sun*2) - (liters_on_mon_thur_sat*2)
    result = liters_on_wednesday
    return result

print(solution())