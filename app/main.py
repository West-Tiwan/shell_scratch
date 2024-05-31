import sys


def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    #print("Logs from your program will appear here!")
    valid_commands = ["exit 0"]

    #REPL loop
    while True:
        sys.stdout.write(f"$ ")
        sys.stdout.flush()
        # Wait for user input
        command = input()
        if command in valid_commands:
            if command == "exit 0":
                sys.exit(0)
        else:
            sys.stdout.write((f"{command}: command not found\r\n").replace('\r\n', '\n'))
            continue



if __name__ == "__main__":
    main()
