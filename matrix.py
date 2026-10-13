MATRIX_STR = '''
7ir
Tsi
h%x
i ?
sM# 
$a 
#t%'''

lines = MATRIX_STR.strip('\n').split('\n')
#convert each row into a list of characters
matrix = [list(row) for row in lines]

num_rows = len(matrix)
num_cols = len(matrix[0])

decoded_msg = ""
was_last_char_alpha = False
decoded_chars = []
#reading through the characters from top to bottom
for col in range(num_cols):
    for row in range(num_rows):
        char = matrix[row][col]
        #check if the characters are letters or symbols
        if char.isalpha():
            decoded_msg += char
            was_last_char_alpha = True
        else:
            if was_last_char_alpha:
                decoded_msg += " "
                was_last_char_alpha = False

print("Decoded Message:", decoded_msg)
