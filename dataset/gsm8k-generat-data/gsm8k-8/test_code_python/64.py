def solution():
    # Define hourly wage and hours worked at main job
    main_wage = 20
    main_hours = 30

    # Calculate earnings from main job
    main_earnings = main_wage * main_hours

    # Define hourly wage and hours worked at second job
    second_wage = main_wage - (0.2 * main_wage)
    second_hours = main_hours / 2

    # Calculate earnings from second job
    second_earnings = second_wage * second_hours

    # Calculate total earnings per week
    total_earnings = main_earnings + second_earnings

    result = total_earnings
    return result

print(solution())