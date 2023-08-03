def process_commands(commands):
    result = []
    queue = []

    for command in commands:
        if command.startswith("push"):
            _, num = command.split()
            queue.append(int(num))
        elif command == "pop":
            result.append(queue.pop(0) if queue else -1)
        elif command == "size":
            result.append(len(queue))
        elif command == "empty":
            result.append(0 if queue else 1)
        elif command == "front":
            result.append(queue[0] if queue else -1)
        elif command == "back":
            result.append(queue[-1] if queue else -1)

    return result

if __name__ == "__main__":
    n = int(input("명령의 개수를 입력하세요: "))
    commands = []
    for _ in range(n):
        commands.append(input())

    output = process_commands(commands)
    for val in output:
        print(val)