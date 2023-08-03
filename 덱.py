from collections import deque

def process_commands(commands):
    dq = deque()
    results = []

    for command in commands:
        if command.startswith('push_front'):
            num = int(command.split()[1])
            dq.appendleft(num)
        elif command.startswith('push_back'):
            num = int(command.split()[1])
            dq.append(num)
        elif command == 'pop_front':
            if dq:
                results.append(dq.popleft())
            else:
                results.append(-1)
        elif command == 'pop_back':
            if dq:
                results.append(dq.pop())
            else:
                results.append(-1)
        elif command == 'size':
            results.append(len(dq))
        elif command == 'empty':
            if dq:
                results.append(0)
            else:
                results.append(1)
        elif command == 'front':
            if dq:
                results.append(dq[0])
            else:
                results.append(-1)
        elif command == 'back':
            if dq:
                results.append(dq[-1])
            else:
                results.append(-1)

    return results