def solution():
    
    # Calculate the number of blue wearers
    blue_wearers = (1/4) * (1/4)

    # Calculate the number of purple wearers
    purple_wearers = (1/3) * blue_wearers

    # Calculate the number of baby wearers
    baby_wearers = (1/3) * purple_wearers

    # Calculate the percentage chance a baby wearing a bow is wearing purple
    percentage_chance = (baby_wearers / purple_wearers) * 100

    # Display the percentage chance
    result = percentage_chance
    return result

print(solution())