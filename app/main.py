import sys


def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    #print("Logs from your program will appear here!")
    valid_commands = ["exit","echo","type"]

    #REPL loop
    while True:
        sys.stdout.write(f"$ ")
        sys.stdout.flush()
        # Wait for user input
        command = input()
        args = command.split(" ")
        if args[0] == "exit":
            if args[1] == "0":
                break
        elif args[0] == "echo":
            sys.stdout.write(" ".join(args[1:]) + "\n")
        elif args[0] == "type":
            if args[1] in valid_commands:
                sys.stdout.write(f"{args[1]} is a shell builtin\n")
            else:
                sys.stdout.write(f"{args[1]} not found\n")
        else:
            sys.stdout.write(f"{command}: command not found\n")



if __name__ == "__main__":
    main()
