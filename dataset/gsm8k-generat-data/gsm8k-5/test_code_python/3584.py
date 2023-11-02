def solution():
    monthly_income = 20 + 40  # Mary earns $20 washing cars and $40 walking dogs each month
    half_income = monthly_income / 2  # Mary puts half of her income away each month
    savings_goal = 150  # Mary wants to save $150
    months_to_reach_goal = savings_goal / half_income  # Calculate how many months it will take to reach the goal

    result = months_to_reach_goal
    return result

print(solution())