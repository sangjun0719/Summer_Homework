def process_commands(commands):
    result = []
    stack = []

    for command in commands:
        if command.startswith("push"):
            _, num = command.split()
            stack.append(int(num))
        elif command == "pop":
            result.append(stack.pop() if stack else -1)
        elif command == "size":
            result.append(len(stack))
        elif command == "empty":
            result.append(0 if stack else 1)
        elif command == "top":
            result.append(stack[-1] if stack else -1)

    return result

if __name__ == "__main__":
    n = int(input("명령의 개수를 입력하세요: "))
    commands = []
    for _ in range(n):
        commands.append(input())

    output = process_commands(commands)
    for val in output:
        print(val)