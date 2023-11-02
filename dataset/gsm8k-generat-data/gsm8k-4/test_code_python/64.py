def solution():
    """James earns $20 an hour while working at his main job. He earns 20% less while working his second job. He works 30 hours at his main job and half that much at his second job. How much does he earn per week?"""
    # Define the hourly wage and number of hours for the main job
    main_wage = 20
    main_hours = 30

    # Define the hourly wage and number of hours for the second job
    second_wage = main_wage * 0.8   # 20% less
    second_hours = main_hours / 2  # half as much

    # Calculate the earnings from the main job and second job
    main_earnings = main_wage * main_hours
    second_earnings = second_wage * second_hours

    # Calculate the total weekly earnings
    weekly_earnings = main_earnings + second_earnings

    # return the result
    result = weekly_earnings
    return result

print(solution())