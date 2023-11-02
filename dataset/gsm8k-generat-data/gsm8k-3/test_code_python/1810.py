def solution():
    """Heisenberg owns a pharmacy. He earned a total of $80 from 100 mg amoxicillin and $60 from 500 mg amoxicillin every week. If each capsule of 100 mg amoxicillin costs $5 and each capsule of 500 mg amoxicillin costs $2, how many capsules of amoxicillin does he sell every 2 weeks?"""
    # Define the cost and amount of each type of amoxicillin sold per week
    AMOX_100_COST = 5
    AMOX_500_COST = 2
    AMOX_100_WEEKLY = 80
    AMOX_500_WEEKLY = 60

    # Calculate the total number of capsules of each type sold per week
    amox_100_capsules = AMOX_100_WEEKLY / AMOX_100_COST
    amox_500_capsules = AMOX_500_WEEKLY / AMOX_500_COST

    # Calculate the total number of capsules sold every 2 weeks
    total_capsules = (amox_100_capsules + amox_500_capsules) * 2

    # Display the total number of capsules sold every 2 weeks
    result = total_capsules
    return result

print(solution())