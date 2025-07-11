from pprint import pprint

FILE_URI=r"example.pyos"
FILE = open(FILE_URI)

blocks_tokens = {"globals","template","func","main"}

FILE_DATA = FILE.read()

def remove_empty_lines(text):
    return "\n".join([line for line in text.splitlines() if line.strip()])    

def get_blocks(DATA):
    global blocks_tokens
    current_block = {}
    for i in  DATA.split("@")[1:]:
        block = i.split("(")[0]
        if block not in blocks_tokens:
            raise SyntaxError(f"Unknown block: {block}")
        block_data=remove_empty_lines(i[len(i.split("(")[0]):]).strip("()")
        current_block[block]= remove_empty_lines(block_data).split("\n")
    return current_block
    


