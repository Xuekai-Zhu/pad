def solution():
    """Police officer A patrols 36 streets in 4 hours. His colleague, officer B, patrols 55 streets in 5 hours. How many streets will both officers patrol in one hour?"""
    # Calculate Officer A's rate of streets patrolled per hour
    rate_a = 36 / 4

    # Calculate Officer B's rate of streets patrolled per hour
    rate_b = 55 / 5

    # Calculate the combined rate of streets patrolled per hour for both officers
    combined_rate = rate_a + rate_b

    # Display the combined rate of streets patrolled per hour
    result = combined_rate
    return result

print(solution())