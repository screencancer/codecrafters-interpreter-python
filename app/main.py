import sys

valid_operators = {
    "=": "EQUAL",
    "!": "BANG",
    "<": "LESS",
    ">": "GREATER",
    "(": "LEFT_PAREN",
    ")": "RIGHT_PAREN",
    "{": "LEFT_BRACE",
    "}": "RIGHT_BRACE",
    "*": "STAR",
    ".": "DOT",
    ",": "COMMA",
    "+": "PLUS",
    "-": "MINUS"
}

def findlinenum(file, char, pointer):
    #Find line of err
    line_num = file.count("\n", 0, file.find(char, pointer - 1)) + 1
    return line_num

def checkString(startIdx, file_contents, pointer):
    pointer = 0
    str = []
    while c != '"':
        pointer += 1
        c = file_contents[pointer]
        str.append(c)

    return 0

def checkNeighbor(file_contents, pointer, c, expression):
        expression += "_"
        print(expression)

        if (pointer + 1 < len(file_contents)):
            nextOp = valid_operators.get(file_contents[pointer + 1])
            expression += nextOp
            print(expression)
            if (expression in valid_operators):
                print(expression)
                return expression

def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    #print("Logs from your program will appear here!", file=testfile)

    #if len(sys.argv) < 3:
        #print("Usage: ./your_program.sh tokenize <filename>", file=testfile)
        #exit(1)

    #command = sys.argv[1]
    #if command != "tokenize":
        #print(f"Unknown command: {command}", file=testfile)
        #exit(1)

    with open("app/testfile.txt") as file:
        file_contents = file.read()

    err = False
    pointer = 0
    while pointer < len(file_contents):
        c = file_contents[pointer]
        pointer += 1
        build_exp(file_contents, pointer, c)
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
        elif c == "=":
            if result == "EQUAL_EQUAL == null":
                pointer += 1
            print(result)
        elif c == "!":
            if result == "BANG_EQUAL != null":
                pointer += 1
            print(result)
        elif c == "<":
            if result == "LESS_EQUAL <= null":
                pointer += 1
            print(result)
        elif c == ">":
            if result == "GREATER_EQUAL >= null":
                pointer += 1
            print(result)
        elif c == "/":
            if result == "EOF  null":
                while file_contents[pointer-1] not in ["\n", ""]:
                    pointer += 1
                    if pointer == len(file_contents):
                        break
            else:
                print(result)
        elif c == " " or c == "\t" or c == "\n":
            pass
        elif c == '"':
            #check if string
            checkString(pointer, file_contents, pointer)
        else:
            err = True
            error_message = f"[line {findlinenum(file_contents, c, pointer)}] " + f"Error: Unexpected character: {c}"
            print(error_message, file=sys.stderr)
    print("EOF  null")
    if err:
        sys.exit(65)
    else:
        sys.exit(0)


def build_exp(file_contents, pointer, c):
    
    expression = valid_operators.get(c)

    checkNeighbor(file_contents, pointer, c, expression)

if __name__ == "__main__":
    main()
