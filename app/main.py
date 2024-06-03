import sys
import os

def main():
    valid_commands = ["exit","echo","type"]
    PATH = os.environ.get('PATH')
    while True:
        sys.stdout.write(f"$ ")
        sys.stdout.flush()
        command = input()
        args = command.split(" ")
        if args[0] == "exit":
            if args[1] == "0":
                break
        elif args[0] == "echo":
            sys.stdout.write(" ".join(args[1:]) + "\n")
        elif args[0] == "type":
            cmd = command.split(" ")[1]
            cmd_path = None
            paths = PATH.split(":")
            for path in paths:
                if os.path.isfile(f"{path}/{cmd}"):
                    cmd_path = f"{path}/{cmd}"
            if cmd in valid_commands:
                sys.stdout.write(f"{cmd} is a shell builtin\n")
            elif cmd_path:
                sys.stdout.write(f"{cmd} is {cmd_path}\n")
            elif cmd not in valid_commands:
                sys.stdout.write(f"{command.split(" ")[1]} not found\n")
        else:
            sys.stdout.write(f"{command}: command not found\n")
            sys.stdout.flush()



if __name__ == "__main__":
    main()
