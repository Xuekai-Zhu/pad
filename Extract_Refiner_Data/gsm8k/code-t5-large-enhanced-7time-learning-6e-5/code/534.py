def solution():
    
    # Define the number of vlogs Emma can make and upload per month
    VLOGS_PER_MONTH = 72

    # Define the number of vlogs Emma was able to make for each week
    vlogs_week1 = 18
    vlogs_week2 = 21
    vlogs_week3 = 15

    # Calculate the total number of vlogs Emma should do to complete the 72 vlogs per month
    total_vlogs = (vlogs_week1 + vlogs_week2 + vlogs_week3) * 4

    # Display the total number of vlogs Emma should do
    result = total_vlogs
    return result

print(solution())