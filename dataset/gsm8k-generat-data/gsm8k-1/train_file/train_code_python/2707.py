def solution():
    """Ofelia joined a saving challenge wherein she has to save twice the amount she saved from the previous month. In January, she saved $10. How much is she going to save in May?"""
    starting_amount = 10
    saving_goal_month = 'May'
    saving_goal_amount = starting_amount * 2 ** 4 # May is 4 months after January
    result = saving_goal_amount
    return result

print(solution())