def solution():
    # Define the attire of 1700s judges and the Bible verse referenced by Orthodox Presbyterians
    judge_attire = "powdered wigs and large robes"
    bible_verse = "1 Timothy 2:8-9"
    prohibited_adornments = ["wigs", "jewelry"]
    # Check if the judge's attire includes prohibited adornments according to the Bible verse
    if any(adornment in judge_attire for adornment in prohibited_adornments):
        result = "yes"
    else:
        result = "no"
    return result

print(solution())