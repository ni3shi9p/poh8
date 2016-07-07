cnt_correct = 0

for i in range(0,5):
    answer, response = raw_input().split(" ")
    if answer == response:
        cnt_correct += 1
else:
    if cnt_correct >= 3:
        print("OK")
    else:
        print("NG")
