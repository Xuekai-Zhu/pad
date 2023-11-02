def solution():
    eggs_per_child = 2
    eggs_per_adult = 3
    number_of_children = 4
    number_of_adults = 2
    days_in_year = 365
	
    total_eggs = (eggs_per_child * number_of_children) + (eggs_per_adult * number_of_adults)
    result = total_eggs * days_in_year
    return result

print(solution())