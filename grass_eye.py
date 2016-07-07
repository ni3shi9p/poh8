length = raw_input()
num_list = map(int, raw_input().split())
num_list.sort()
print num_list[len(num_list) / 2]
