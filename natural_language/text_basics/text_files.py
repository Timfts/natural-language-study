
def write_file():
  my_file = open("data/myfile.txt", "a+")
  my_file.write("\n my first file")
  my_file.close()


def read_file():
  my_file = open("data/myfile.txt", "r")
  fileLines = my_file.readlines()
  firstLine = fileLines[0]
  print(firstLine)
  """ release the file """
  my_file.close()