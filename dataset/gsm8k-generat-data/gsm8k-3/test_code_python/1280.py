def solution():
    """Honey earned $80 a day. Every day, she spent part of her pay and saved the rest. After 20 days of work, she spent $1360. How much did Honey save in 20 days?"""
    # Define the amount of money Honey earns and the amount she spent
    DAILY_EARNINGS = 80
    SPENT = 1360

    # Calculate the total amount of money Honey earned in 20 days
    total_earnings = DAILY_EARNINGS * 20

    # Calculate the amount of money Honey saved in 20 days
    saved = total_earnings - SPENT

    # Display the amount Honey saved
    result = saved
    return result

print(solution())