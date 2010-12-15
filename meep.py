import sys

def main():
  if len(sys.argv) != 2:
    print("Please provide a filename.")
    sys.exit(1)
  print("Meep meep!")

if __name__ == '__main__':
  main()
