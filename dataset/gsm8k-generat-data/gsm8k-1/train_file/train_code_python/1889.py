def solution():
    """Jane, Kyla, and Anthony have summer jobs in a resort. Their task is to fold guests' towels. Jane can fold 3 towels in 5 minutes. Kyla can fold 5 towels in 10 minutes, and Anthony can fold 7 towels in 20 minutes. If they all fold towels together, how many towels can they fold in one hour?"""
    jane_towels_per_min = 3 / 5
    kyla_towels_per_min = 5 / 10
    anthony_towels_per_min = 7 / 20
    total_towels_per_min = jane_towels_per_min + kyla_towels_per_min + anthony_towels_per_min
    towels_per_hour = total_towels_per_min * 60
    result = towels_per_hour
    return result

print(solution())