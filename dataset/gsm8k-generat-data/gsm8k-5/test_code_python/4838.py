def solution():
    # Total kilos collected for 2 weeks by one section
    kilos_collected_per_section = 280

    # Total kilos collected for 2 weeks by all 6 sections
    total_kilos_collected = kilos_collected_per_section * 6

    # Total kilos collected after 3 weeks
    total_kilos_after_3_weeks = total_kilos_collected + (kilos_collected_per_section * 3)

    # Target for the recycling drive
    target_kilos = total_kilos_after_3_weeks + 320

    result = target_kilos
    return result

print(solution())