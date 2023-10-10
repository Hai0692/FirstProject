import re
token_patterns = [
    (r'\bvoid|int|for\b', 'keyword'),
    (r'[a-zA-Z][a-zA-Z0-9_]*', 'identifier'),
    (r'[0-9][0-9]*(\.[0-9]+)?([eE][-+]?[0-9]+)?', 'num'), 
    (r'[+]', '+'),
    (r'[==]', '='),
    (r'[<]', '<'),
    (r'\)', ')'),
    (r'\(', '('),
    (r'{', '{'),
    (r'}', '}'),
    (r'\[', '['),
    (r'\]', ']'),
    (r';', ';'),
    (r'\.', 'Error'),
]

# Read the input from a file
input_file_path = 'sample_input.txt'
with open(input_file_path, 'r') as file:
    code = file.read()

# Tokenize the input code and print in the desired format
line_number = 1 #sử dụng để theo dõi số dòng trong mã đầu vào.
for match in re.finditer('|'.join(f'({pattern})' for pattern, _ in token_patterns), code):
    token_type = None
    lexeme = match.group()# Dòng này trích xuất văn bản trùng khớp (từ vựng) từ đối tượng khớp hiện tại và gán nó cho biến lexeme.
    for pattern, ttype in token_patterns: # Vòng lặp bên trong này lặp lại từng mẫu biểu thức chính quy và loại mã thông báo được liên kết của nó 
        if re.match(pattern, lexeme): #kiểm tra xem từ vựng hiện tại có khớp với mẫu hiện tại hay không
            token_type = ttype
            break

    if token_type: #kiểm tra xem biến token_type đã được xác định cho từ vựng hiện tại hay chưa. Nếu có, nó sẽ thực hiện các hành động dựa trên loại của từ vựng.
        if token_type == 'num':
            print(f'num : {lexeme}')
        elif token_type == 'Error':
            print(f'Error : {lexeme}')  # Treat period '.' as an error
        else:
            print(f'{token_type} : {lexeme}')
    elif lexeme == '\n':
        line_number += 1
    else:
        # if lexeme == '}' or lexeme == '{':-
        #        print(':')
        print(f'{lexeme} : {lexeme}')
