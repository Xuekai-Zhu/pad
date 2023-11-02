def solution():
    drawings_on_first_page = 5
    drawings_on_second_page = drawings_on_first_page + 5
    drawings_on_third_page = drawings_on_second_page + 5
    drawings_on_fourth_page = drawings_on_third_page + 5
    drawings_on_fifth_page = drawings_on_fourth_page + 5
    total_drawings = drawings_on_first_page+ drawings_on_second_page+ drawings_on_third_page+ drawings_on_fourth_page+ drawings_on_fifth_page
    result = total_drawings
    
    return result

print(solution())