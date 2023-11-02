def solution():
    """Max was doing homework in three different subjects. It took him 20 minutes to finish tasks from biology and two times more time to finish history. Geography took him the most time, three times more than history. How much time did Max spend on doing his homework?"""
    # Define the time taken for Biology
    bio_time = 20

    # Calculate the time taken for History
    his_time = bio_time * 2

    # Calculate the time taken for Geography
    geo_time = his_time * 3

    # Calculate the total time taken for homework
    total_time = bio_time + his_time + geo_time

    # Display the total time taken
    result = total_time
    return result

print(solution())