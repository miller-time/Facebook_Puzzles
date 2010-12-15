import sys

def read_file():
  if not sys.argv[1]:
    sys.exit(1)
  return open(sys.argv[1], 'rU').read()

def do_output(number):
  for i in range(1,number):
    if i%3 == 0 and i%5 != 0:
      print("Hoppity")
    elif i%5 == 0 and i%3 != 0:
      print("Hophop")
    elif i%3 == 0 and i%5 == 0:
      print("Hop")

def main():
  if len(sys.argv) != 2:
    print("Please provide a filename.")
    sys.exit(1)
  number_string = read_file()
  do_output(int(number_string))

if __name__ == '__main__':
  main()
