def solution():
     tabs_opened = 400
     first_fraction_closed = 1/4
     second_fraction_closed = 2/5
     third_fraction_closed = 1/2
     first_tabs_closed = tabs_opened * first_fraction_closed
     second_tabs_closed = (tabs_opened - first_tabs_closed) * second_fraction_closed
     third_tabs_closed = (tabs_opened - first_tabs_closed - second_tabs_closed) * third_fraction_closed
     total_tabs_closed = first_tabs_closed + second_tabs_closed + third_tabs_closed
     remaining_tabs = tabs_opened - total_tabs_closed
     result = remaining_tabs
     return result

print(solution())