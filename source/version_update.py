import sys

curr_ver=sys.argv[1]
next_num=curr_ver.split('.')
next_num[len(next_num)-1]=str(int(next_num[len(next_num)-1])+1)
new_ver='.'.join(next_num)
print(new_ver)