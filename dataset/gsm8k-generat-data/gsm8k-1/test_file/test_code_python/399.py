Sorry, I cannot provide a solution to the Samantha's last name question as it has insufficient information to determine the length of Bobbie's last name or Jamie's last name. 

Regarding the Mel's air conditioner question, we can use the following solution:

def solution():
    """Mel uses a 900-watt air conditioner for 8 hours a day. This means that each hour the AC uses 900 watts of energy. If he reduces the time he uses the air conditioner by 5 hours a day, how many kilowatts of electric energy will he save in 30 days?"""
    ac_wattage = 900
    ac_hours = 8
    ac_energy_per_day = ac_wattage * ac_hours / 1000 # convert to kilowatt-hours
    
    reduced_hours = ac_hours - 5
    reduced_energy_per_day = ac_wattage * reduced_hours / 1000
    
    daily_energy_savings = ac_energy_per_day - reduced_energy_per_day
    
    total_savings = daily_energy_savings * 30 # 30 days
    
    result = total_savings
    return result

print(solution())