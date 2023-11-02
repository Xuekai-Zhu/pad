def solution():
    
    gecko_count = 5
    gecko_insect_count = 6
    total_gecko_insect_count = gecko_count * gecko_insect_count

    lizard_count = 3
    lizard_insect_count = 2 * gecko_insect_count
    total_lizard_insect_count = lizard_count * lizard_insect_count

    total_insect_count = total_gecko_insect_count + total_lizard_insect_count
    result = total_insect_count
    return result

print(solution())