def solution():
    """Vincent’s washer broke so he had to go to the laundromat. On Wednesday he washed six loads of clothes. The next day he had time to wash double the number of loads he did the day before. On Friday he had a test and could only manage half of the loads he did on Thursday. On Saturday the laundromat closed at noon and he could only wash a third of the loads of laundry he did on Wednesday. How many loads of laundry had he washed that week?"""
    wednesday_loads = 6
    thursday_loads = wednesday_loads * 2
    friday_loads = thursday_loads / 2
    saturday_loads = wednesday_loads / 3
    total_loads = wednesday_loads + thursday_loads + friday_loads + saturday_loads
    result = total_loads
    return result

print(solution())