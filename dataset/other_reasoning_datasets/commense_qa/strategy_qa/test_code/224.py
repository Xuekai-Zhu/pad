def solution():
    # Define relevant information
    robert_stack_show_title = "Unsolved Mysteries"
    robert_stack_show_seasons = 14
    mysterious_events_explored = True
    tower_of_london_history = True
    edward_iv_heirs_mystery = True
    
    # Check if Tower of London and Edward IV mystery would fit the show's theme and time period
    if mysterious_events_explored and tower_of_london_history and edward_iv_heirs_mystery and robert_stack_show_seasons == 14:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())