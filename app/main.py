import sys


def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    #print("Logs from your program will appear here!")
    valid_commands = []
    # Uncomment this block to pass the first stage
    sys.stdout.write("$ ")
    sys.stdout.flush()

    # Wait for user input
    command = input()
    if command in valid_commands:
        print('hello')
    else:
        print((f"{command}: command not found\r\n").replace('\r\n', '\n'))


if __name__ == "__main__":
    main()
