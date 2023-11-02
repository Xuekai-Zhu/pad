def solution():
    tony_bennet_middle_name = "Dominick"
    former_ufc_champions_with_middle_name = ["Dominick Cruz", "Another UFC Champion"]
    if tony_bennet_middle_name in former_ufc_champions_with_middle_name:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())