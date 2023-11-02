def solution():
    """Cloud 9 Diving Company has taken individual bookings worth $12,000 and group bookings worth $16,000. Some people have cancelled at the last minute. $1600 has had to be returned to them. How much money has the sky diving company taken altogether?"""
    # Define the total revenue before cancellations
    total_revenue = 12000 + 16000

    # Subtract the amount returned due to cancellations
    final_revenue = total_revenue - 1600

    # Display the final revenue
    result = final_revenue
    return result

print(solution())