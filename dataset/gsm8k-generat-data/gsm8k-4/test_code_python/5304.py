def solution():
    """Gumball was counting his water intake for the previous week. He checked his list and saw that he had drank 60 liters of water for the week. He drank nine liters of water on Monday, Thursday and Saturday and 8 liters of water on Tuesday, Friday and Sunday. Unfortunately, no data was input on Wednesday. How many liters of water did he drink on Wednesday?"""
    # Define the total amount of water drank for the week
    total_water = 60

    # Define the amount of water drank on Monday, Thursday and Saturday
    mts_water = 9

    # Define the amount of water drank on Tuesday, Friday and Sunday
    tfs_water = 8

    # Calculate the total amount of water drank from Monday to Sunday (excluding Wednesday)
    mtsfs_water = (mts_water * 3) + (tfs_water * 3)

    # Calculate the amount of water drank on Wednesday
    wed_water = total_water - mtsfs_water

    result = wed_water
    return result

print(solution())