def solution():
    nathan_letters_per_hour = 25
    jacob_letters_per_hour = nathan_letters_per_hour * 2
    total_hours = 10
    total_letters = jacob_letters_per_hour + nathan_letters_per_hour
    result = total_letters * total_hours
    
    return result

print(solution())