length = int(raw_input())
progress = int(raw_input())

line = ""

for i in range(1,length + 1):
    line += "+" if i == progress else "-"

print line
