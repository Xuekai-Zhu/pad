def solution():
    sheets_per_folder = 10
    stickers_per_sheet_red = 3
    stickers_per_sheet_green = 2
    stickers_per_sheet_blue = 1
    folders = 3
    total_stickers = (sheets_per_folder * stickers_per_sheet_red) + (sheets_per_folder * stickers_per_sheet_green) + (sheets_per_folder * stickers_per_sheet_blue)
    result = total_stickers
    
    return result

print(solution())