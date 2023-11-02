def solution():
    """A rope has a length of 200 meters. Stefan cuts the rope into four equal parts, gives his mother half of the cut pieces, and subdivides the remaining pieces into two more equal parts. What's the length of each piece?"""
    rope_length = 200
    num_parts = 4
    parts_given_to_mother = num_parts / 2
    
    remaining_parts = num_parts - parts_given_to_mother
    subdivided_parts = remaining_parts * 2
    
    length_per_part = rope_length / num_parts
    final_length_per_part = length_per_part / subdivided_parts
    
    result = final_length_per_part
    return result

print(solution())