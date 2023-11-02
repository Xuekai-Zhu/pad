def solution():
    total_cattle = 100  # Assuming all cattle are either male or female, and 100% = all cattle
    male_percentage = 40  # 40% of cattle are male
    male_cattle = (male_percentage / 100) * total_cattle  # Calculate the number of male cattle
    female_cattle = total_cattle - male_cattle  # Calculate the number of female cattle

    # Calculate the total milk produced by the female cattle
    female_milk = female_cattle * 2  # Each female cow produces 2 gallons of milk per day
    total_milk = female_milk  # Only female cattle produce milk

    # If there are 50 male cows, subtract their contribution to the total cattle count
    if male_cattle >= 50:
        male_cattle -= 50
        total_cattle -= 50
        female_cattle = total_cattle - male_cattle
        female_milk = female_cattle * 2
        total_milk = female_milk
    
    result = total_milk
    return result

print(solution())