def solution():
    
    total_square_footage = 16000
    initial_smaller_house = 5200
    initial_larger_house = 7300
    total_initial_square_footage = initial_smaller_house + initial_larger_house
    expanded_smaller_house = total_square_footage - initial_larger_house
    additional_square_footage = expanded_smaller_house - initial_smaller_house
    result = additional_square_footage
    return result

print(solution())