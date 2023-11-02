def solution():
    morning_hours = 2  # Donna walks dogs for 2 hours every morning
    morning_pay = 10  # Donna makes $10.00 an hour in the morning
    morning_total = morning_hours * morning_pay * 5  # Calculate Donna's earnings from morning dog walking

    after_school_hours = 2  # Donna works at the card shop for 2 hours after school
    after_school_pay = 12.5  # Donna makes $12.50 an hour at the card shop
    after_school_total = after_school_hours * after_school_pay * 5  # Calculate Donna's earnings from working at the card shop

    weekend_babysitting_hours = 4  # Donna is guaranteed 4 hours every Saturday babysitting
    weekend_babysitting_pay = 10  # Donna makes $10.00 an hour babysitting on the weekends
    weekend_babysitting_total = weekend_babysitting_hours * weekend_babysitting_pay * 2  # Calculate Donna's earnings from weekend babysitting

    # Calculate the total amount of money Donna made over 7 days
    total_earnings = morning_total + after_school_total + weekend_babysitting_total
    result = total_earnings
    return result

print(solution())