def solution():
     total_dice_needed = 14
     dice_owned_by_mark = 10
     percent_12_sided_dice_mark = .6
     dice_owned_by_james = 8
     percent_12_sided_dice_james = .75
     dice_12_sided_owned_by_mark = dice_owned_by_mark * percent_12_sided_dice_mark
     dice_12_sided_owned_by_james = dice_owned_by_james * percent_12_sided_dice_james
     dice_12_sided_needed = total_dice_needed - (dice_12_sided_owned_by_mark + dice_12_sided_owned_by_james)
     result = dice_12_sided_needed
    
     return result

print(solution())