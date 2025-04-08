# front.py - a lexical analyzer for simple arithmetic expressions

# Character classes
LETTER = 0
DIGIT = 1
UNKNOWN = 99

# Token codes
INT_LIT = 10
IDENT = 11
ASSIGN_OP = 20
ADD_OP = 21
SUB_OP = 22
MULT_OP = 23
DIV_OP = 24
LEFT_PAREN = 25
RIGHT_PAREN = 26
EOF = -1

# Global variables
char_class = None
lexeme = ''
next_char = ''
next_token = None
input_data = ''
char_index = 0

def add_char():
    global lexeme
    lexeme += next_char

def get_char():
    global next_char, char_class, char_index, input_data
    if char_index < len(input_data):
        next_char = input_data[char_index]
        char_index += 1
        if next_char.isalpha():
            char_class = LETTER
        elif next_char.isdigit():
            char_class = DIGIT
        else:
            char_class = UNKNOWN
    else:
        next_char = ''
        char_class = EOF

def get_non_blank():
    while next_char.isspace():
        get_char()

def lookup(ch):
    global next_token
    if ch == '(':
        add_char()
        next_token = LEFT_PAREN
    elif ch == ')':
        add_char()
        next_token = RIGHT_PAREN
    elif ch == '+':
        add_char()
        next_token = ADD_OP
    elif ch == '-':
        add_char()
        next_token = SUB_OP
    elif ch == '*':
        add_char()
        next_token = MULT_OP
    elif ch == '/':
        add_char()
        next_token = DIV_OP
    elif ch == '=':
        add_char()
        next_token = ASSIGN_OP
    else:
        add_char()
        next_token = EOF
    return next_token

def lex():
    global lexeme, next_token
    lexeme = ''
    get_non_blank()

    if char_class == LETTER:
        add_char()
        get_char()
        while char_class == LETTER or char_class == DIGIT:
            add_char()
            get_char()
        next_token = IDENT

    elif char_class == DIGIT:
        add_char()
        get_char()
        while char_class == DIGIT:
            add_char()
            get_char()
        next_token = INT_LIT

    elif char_class == UNKNOWN:
        lookup(next_char)
        get_char()

    elif char_class == EOF:
        next_token = EOF
        lexeme = 'EOF'

    print(f"Next token is: {next_token}, Next lexeme is {lexeme}")
    return next_token

def main():
    global input_data
    try:
        with open("C:\\Users\\musta\\source\\repos\\PythonApplication7\\front.in", "r") as file:
            input_data = file.read()
        get_char()
        while True:
            if lex() == EOF:
                break
    except FileNotFoundError:
        print("ERROR - cannot open front.in")

if __name__ == "__main__":
    main()
