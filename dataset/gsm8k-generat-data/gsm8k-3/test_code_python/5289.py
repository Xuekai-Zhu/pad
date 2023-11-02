def solution():
    """John decides to stop delivering the newspapers he is supposed to deliver and instead steals them to recycle them for cash.  The Monday-Saturday papers weigh 8 ounces each.  The Sunday paper weighs twice as much.  He is supposed to deliver 250 papers a day.  He doesn't deliver them for 10 weeks.  If one ton of paper recycles for $20, how much did he make?"""
    # Define the weight of each type of paper
    MONDAY_TO_SATURDAY_WEIGHT = 8
    SUNDAY_WEIGHT = MONDAY_TO_SATURDAY_WEIGHT * 2

    # Define the number of papers John was supposed to deliver per day
    NUM_PAPERS_PER_DAY = 250

    # Define the number of weeks John didn't deliver papers
    NUM_WEEKS = 10

    # Calculate the total weight of Monday to Saturday papers
    monday_to_saturday_weight = MONDAY_TO_SATURDAY_WEIGHT * NUM_PAPERS_PER_DAY * 6 * NUM_WEEKS

    # Calculate the total weight of Sunday papers
    sunday_weight = SUNDAY_WEIGHT * NUM_PAPERS_PER_DAY * NUM_WEEKS

    # Calculate the total weight of all papers
    total_weight = monday_to_saturday_weight + sunday_weight

    # Convert the weight to tons
    total_tons = total_weight / 16 / 2000

    # Calculate the total earnings from recycling
    total_earnings = total_tons * 20

    # Display the total earnings
    result = total_earnings
    return result

print(solution())