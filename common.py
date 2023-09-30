
def load_file_text(file_name):
    f = open(file_name, "r")
    return f.read()

def write_file(file_name, text):
    f = open(file_name, "w")
    f.write(text)
    f.close()