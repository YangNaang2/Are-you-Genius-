import sys
stack_l = list(input())
#abcd
stack_r = []
n = int(input())
#3
for i in range(n):
    command = sys.stdin.readline().split()
    # p x  / l / p y
    if command[0] =="L" and stack_l:
        stack_r.append(stack_l.pop())
    elif command[0] == "D" and stack_r:
        stack_l.append(stack_r.pop())
    elif command[0] == "B" and stack_l:
        stack_l.pop()
    elif command[0] =="P":
        stack_l.append(command[1])

print("".join(stack_l + list(reversed(stack_r))))
