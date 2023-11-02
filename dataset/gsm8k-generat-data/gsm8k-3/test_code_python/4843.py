def solution():
    """Josh has soccer practice on Monday, Wednesday, and Friday from 3:00 p.m. to 5:00 p.m.  He has band practice on Tuesday and Thursday from 3:30 p.m. to 5:00 p.m.  From Monday to Friday, how many hours does Josh spend on extracurricular activities?"""
    # Define the start and end times of each activity
    soccer_start = datetime.datetime.strptime('15:00', '%H:%M')
    soccer_end = datetime.datetime.strptime('17:00', '%H:%M')
    band_start = datetime.datetime.strptime('15:30', '%H:%M')
    band_end = datetime.datetime.strptime('17:00', '%H:%M')

    # Get the number of hours Josh spends on soccer
    soccer_hours = (soccer_end - soccer_start).total_seconds() / 3600.0
    # Round to two decimal places
    soccer_hours = round(soccer_hours, 2)

    # Get the number of hours Josh spends on band
    band_hours = (band_end - band_start).total_seconds() / 3600.0
    # Round to two decimal places
    band_hours = round(band_hours, 2)

    # Calculate the total number of hours Josh spends on extracurricular activities
    total_hours = soccer_hours * 3 + band_hours * 2

    # Display the total number of hours
    result = total_hours
    return result

print(solution())