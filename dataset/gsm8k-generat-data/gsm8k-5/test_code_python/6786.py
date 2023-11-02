def solution():
    current_length = 2  # Sandy's fingernails are currently 2 inches long
    growth_rate = 0.1  # Sandy's fingernails grow by 0.1 inches per month
    target_length = 26  # The world record for longest fingernails is 26 inches
    months_to_reach_target_length = (target_length - current_length) / growth_rate  # Calculate how many months it will take for Sandy to reach the target length
    years_to_reach_target_length = months_to_reach_target_length / 12  # Convert months to years
    age_when_reaching_record = 12 + years_to_reach_target_length  # Sandy just turned 12 this month

    result = age_when_reaching_record
    return result

print(solution())