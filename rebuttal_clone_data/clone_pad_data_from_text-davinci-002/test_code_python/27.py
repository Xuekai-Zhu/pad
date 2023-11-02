def solution():
     """Brennan was researching his school project and had to download files from the internet to his computer to use for reference. After downloading 800 files, he deleted 70% of them because they were not helpful. He downloaded 400 more files but again realized that 3/5 of them were irrelevant. How many valuable files was he left with after deleting the unrelated files he downloaded in the second round?"""

    files_downloaded_first_round = 800
    deleted_first_round = 800 * .7
    total_deleted = deleted_first_round + (400 * .6)
    files_left = files_downloaded_first_round - total_deleted
    result = files_left
    return result

print(solution())