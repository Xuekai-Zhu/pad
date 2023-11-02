def solution():
     first_class = 10
     business_class = 30
     economy_class = 50
     economy_class_filled = economy_class / 2
     total_filled = economy_class_filled + first_class + business_class
     total_seats = first_class + business_class + economy_class
     business_class_vacant = total_seats - total_filled
     result = business_class_vacant
     return result

print(solution())