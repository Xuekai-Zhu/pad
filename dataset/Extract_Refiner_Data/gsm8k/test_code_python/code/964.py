def solution():
    
    # Define the number of racquets and the time it takes to strung each type of racquet
    num_racquets = 12
    strung_synthetic_gut = 3
    strung_polyester_string = 5
    strung_hybrid_set = 4
    strung_synthetic_gut_time = 15
    strung_polyester_string_time = 22
    strung_hybrid_set_time = 18

    # Calculate the total time it takes to strung all racquets
    total_strung_time = (strung_synthetic_gut * strung_synthetic_gut_time) + (strung_polyester_string * strung_polyester_string_time) + (strung_hybrid_set * strung_hybrid_set_time)

    # Calculate the total time it takes to string all racquets
    total_string_time = total_strung_time + strung_synthetic_gut + strung_polyester_string + strung_hy

print(solution())