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
    ">=": "GREATER_EQUAL",
    "!=": "BANG_EQUAL",
    "<=": "LESS_EQUAL",
    "-=": "MINUS_EQUAL",
    "*=": "STAR_EQUAL",
    "+=": "PLUS_EQUAL"
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
            #If nextop is out of bounds return last char alone without checking
            try:
                nextOp = valid_operators.get(file_contents[pointer+1])
            except:
                print(f"List out of bounds at {pointer} in {c}")
                return c, pointer

            tempexp += nextOp
            cList = list(valid_double_operators.keys());

            iteration = 0;
            for values in cList:
                #print(iteration)
                if(tempexp == valid_double_operators.get(values)):
                    #print(tempexp + " Is Valid double operator")
                    valid = True
                    try:
                        pointer += 1;
                        return tempexp + " " + cList[iteration] + " null", pointer
                    except:
                        print(f"List out of bounds at {pointer} in {c}")
                elif(iteration == len(valid_double_operators)-1):
                    #print(expression)
                    #print("final")
                    return expression, pointer

                iteration+=1


def main():
    with open("app/testfile.txt") as file:
        file_contents = file.read()

    err = False
    pointer = 0
    while pointer < len(file_contents):
        c = file_contents[pointer]
        if(valid_operators.get(c) == None):
            print(f"Invalid at line number: {findlinenum(file_contents, c, pointer)}")
            err = True
            break
        else:
            expression, pointer = build_exp(file_contents, pointer, c)
            pointer += 1
            print(expression)
    print("EOF  null")
    if err:
        sys.exit(65)
    else:
        sys.exit(0)


def build_exp(file_contents, pointer, c):
    
    expression = valid_operators.get(c)

    #print(f"Pointer at {pointer}")
    #print(file_contents[pointer])

    expression, pointer = checkNeighbor(file_contents, pointer, c, expression)
    return expression, pointer

if __name__ == "__main__":
    main()
