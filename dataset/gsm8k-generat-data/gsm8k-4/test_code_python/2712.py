def solution():
    """Caprice is taking piano lessons. Her mother pays the teacher $10 for every half-hour of teaching her daughter. If Caprice is taking one lesson per week, and the lesson lasts 1 hour, how much money would the teacher earn in 5 weeks?"""
    # Define the rate of pay per half-hour
    rate_per_half_hour = 10

    # Calculate the total pay per hour
    pay_per_hour = rate_per_half_hour * 2

    # Calculate the total pay per lesson
    pay_per_lesson = pay_per_hour * 1

    # Calculate the total earnings for 5 lessons
    total_earnings = pay_per_lesson * 5

    # Return the total earnings
    result = total_earnings
    return result

print(solution())