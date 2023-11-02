def solution():
    """Jane, Kyla, and Anthony have summer jobs in a resort. Their task is to fold guests' towels. Jane can fold 3 towels in 5 minutes. Kyla can fold 5 towels in 10 minutes, and Anthony can fold 7 towels in 20 minutes. If they all fold towels together, how many towels can they fold in one hour?"""
    jane_towel_rate = 3/5 # towels per minute
    kyla_towel_rate = 5/10 # towels per minute
    anthony_towel_rate = 7/20 # towels per minute
    total_rate = jane_towel_rate + kyla_towel_rate + anthony_towel_rate # towels per minute
    towels_per_hour = total_rate * 60 # towels per hour
    result = towels_per_hour
    return result

print(solution())