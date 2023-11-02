def solution():
    """Kim's dad would buy her 2 candy bars a week. She would eat 1 candy bar every 4 weeks, saving the rest. After 16 weeks, how many candy bars did Kim have saved?"""
    # Calculate the total number of candy bars bought in 16 weeks
    total_bought = 2 * 16

    # Calculate the total number of candy bars eaten in 16 weeks
    total_eaten = 16 // 4

    # Calculate the total number of candy bars saved after 16 weeks
    total_saved = total_bought - total_eaten

    result = total_saved
    return result

print(solution())