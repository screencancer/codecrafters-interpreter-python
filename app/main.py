import sys


def findlinenum(file, char):
    #Find line of err
    line_num = file.count("\n", 0, file.find(char)) + 1
    return line_num


def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!", file=sys.stderr)

    if len(sys.argv) < 3:
        print("Usage: ./your_program.sh tokenize <filename>", file=sys.stderr)
        exit(1)

    command = sys.argv[1]
    filename = sys.argv[2]

    if command != "tokenize":
        print(f"Unknown command: {command}", file=sys.stderr)
        exit(1)

    with open(filename) as file:
        file_contents = file.read()

    err = False
    pointer = 0
    for c in file_contents:
        pointer += 1
        if c == "(":
            print("LEFT_PAREN ( null")
        elif c == ")":
            print("RIGHT_PAREN ) null")
        elif c == "{":
            print("LEFT_BRACE { null")
        elif c == "}":
            print("RIGHT_BRACE } null")
        elif c == "*":
            print("STAR * null")
        elif c == ".":
            print("DOT . null")
        elif c == ",":
            print("COMMA , null")
        elif c == "+":
            print("PLUS + null")
        elif c == "-":
            print("MINUS - null")
        elif c == ";":
            print("SEMICOLON ; null")
        elif c == "/":
            print("SLASH / null")
        elif c == "/":
            print("SLASH / null")
        elif c == "=":
            if pointer + 1 < len(file_contents):
                if file_contents[pointer + 1] == "=":
                    print("EQUAL_EQUAL == null")
            print("EQUAL = null")


        else:
            err = True
            error_message = f"[line {findlinenum(file_contents, c)}] " + f"Error: Unexpected character: {c}"
            print(error_message, file=sys.stderr)
    print("EOF  null")
    if err:
        sys.exit(65)
    else:
        sys.exit(0)


if __name__ == "__main__":
    main()
