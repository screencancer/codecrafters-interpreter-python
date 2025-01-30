import sys

valid_operators = {
    "=": "EQUAL = null",
    "!": "BANG ! null",
    "<": "LESS < null",
    ">": "GREATER > null ",
    "(": "LEFT_PAREN ( null",
    ")": "RIGHT_PAREN ) null",
    "{": "LEFT_BRACE { null",
    "}": "RIGHT_BRACE } null",
    "*": "STAR * null",
    ".": "DOT . null",
    ",": "COMMA , null",
    "+": "PLUS + null",
    "-": "MINUS - null"
}

valid_double_operators = {
    "==": "EQUAL_EQUAL == null",
    ">=": "GREATER_EQUAL >= null",
    "!=": "BANG_EQUAL != null",
    "<=": "LESS_EQUAL <= null"
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
        valid = False

        tempexp = expression + "_"
        #print(tempexp)

        if (pointer < len(file_contents)):
            nextOp = valid_operators.get(file_contents[pointer])
            tempexp += nextOp
            c = list(valid_double_operators.keys());

            iteration = 0;

            for values in c:
                #print(iteration)
                if(tempexp == valid_double_operators.get(values)):
                    #print(tempexp + " Is Valid double operator")
                    valid = True
                    return tempexp
                elif(iteration == len(valid_double_operators)-1):
                    #print(expression)
                    #print("final")
                    return expression

                iteration+=1


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
        expression = build_exp(file_contents, pointer, c)
        print(expression)
    print("EOF  null")
    if err:
        sys.exit(65)
    else:
        sys.exit(0)


def build_exp(file_contents, pointer, c):
    
    expression = valid_operators.get(c)

    expression = checkNeighbor(file_contents, pointer, c, expression)
    return expression

if __name__ == "__main__":
    main()
