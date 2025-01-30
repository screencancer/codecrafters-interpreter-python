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

valid_double_operators = {
    "==": "EQUAL_EQUAL",
    ">=": "GREATER_EQUAL"
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

        if (pointer < len(file_contents)):
            nextOp = valid_operators.get(file_contents[pointer])
            expression += nextOp
            c = list(valid_double_operators.keys());
            for values in c:
                print(valid_double_operators.get(values) + " test " + expression)
                if(expression == valid_double_operators.get(values)):
                    print(expression + " Is Valid double operator")

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
