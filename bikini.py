length = raw_input()
before = list(raw_input())
kuso_shiyou_henkou = list(raw_input())

for i in range(0, len(before)):
    item = before.pop()
    try:
        kuso_shiyou_henkou.remove(item)
    except:
        continue

print(len(kuso_shiyou_henkou))
