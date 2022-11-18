def logger(id):
    with open('filestring.txt', 'a') as data:
        rasparse = ", ".join(map(str, (id)))
        rasparse = rasparse + ";\n\n"
        data.write(str(rasparse))
    with open('filecolumn.txt', 'a') as data:
        rasparse = ",\n".join(map(str, (id)))
        rasparse = rasparse + ";\n\n"
        data.write(str(rasparse))

def reader():
    with open("filecolumn.txt", "r") as f:
        for line in f:
            print(line)