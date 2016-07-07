weekly_event = int(raw_input()) * 2
goal_number = int(raw_input())
surplus = 0 if goal_number % weekly_event == 0 else 1

print(str(goal_number / weekly_event + surplus))
    
