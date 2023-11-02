def solution():
    """James earns $20 an hour while working at his main job. He earns 20% less while working his second job. He works 30 hours at his main job and half that much at his second job. How much does he earn per week?"""
    # Define James' main job hourly wage and number of hours worked
    main_wage = 20
    main_hours = 30

    # Define James' second job hourly wage and number of hours worked
    second_wage = main_wage * 0.8
    second_hours = main_hours / 2

    # Calculate James' earnings from his main job
    main_earnings = main_wage * main_hours

    # Calculate James' earnings from his second job
    second_earnings = second_wage * second_hours

    # Calculate James' total weekly earnings
    total_earnings = main_earnings + second_earnings

    result = total_earnings
    return result

print(solution())