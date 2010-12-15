import sys, re

def parse_file():
  if not sys.argv[1]:
    sys.exit(1)
  # open file
  file_string = open(sys.argv[1]).read()
  # find first newline
  first_newline = file_string.find('\n')
  if first_newline == -1:
    print("parse error.")
    sys.exit(1)
  # first line should just be n
  n = int(file_string[:first_newline])
  # remove first line
  rest = file_string[first_newline+1:]
  # turn rest of file into list of lines
  file_list = rest.split('\n')
  liar_dict = get_dict(file_list, n)
  solve_it(liar_dict, n)
    
def find_accuser(string):
  match = re.search(r'(\w+)\s+(\d+)', string)
  if not match:
    print("regex error.")
    sys.exit(1)
  return (match.group(1), int(match.group(2)))

def get_dict(file_list, n):
  liar_dict = {}
  current_line = 0
  # n times, need to get accuser, get m, get list of names
  for i in range(n):
    accuser, m = find_accuser(file_list[current_line])
    liars = []
    for i in range(m):
      # add the name a line below the current line
      liars.append(file_list[current_line + i + 1])
    liar_dict[accuser] = liars
    # increment by 1 for current line, plus m
    current_line = current_line + m + 1
  return liar_dict

def solve_it(liar_dict, n):
  # arbitrarily pick a person
  first_liar = liar_dict.keys()[0]
  # add them to the liars
  liars = [first_liar,]
  honest = []
  while(len(liars) + len(honest) < n):
    # step through the liars..
    for liar in liars:
      # get folk liar has accused
      honest_folk = liar_dict[liar]
      # he's a liar, so they're actually honest
      for good in honest_folk:
        if good not in honest:
          # add em to list if not already there
          honest.append(good)
          print("found an honest! "+good)
    # and the honest folk..
    for good in honest:
      # get folk good has accused
      liar_folk = liar_dict[good]
      # he's honest, so they're liars
      for liar in liar_folk:
        if liar not in liars:
          liars.append(liar)
          print("found a liar! "+liar)
  print("liars..")
  print(liars)
  print("honest..")
  print(honest)

def main():
  if len(sys.argv) != 2:
    print("Please provide a filename.")
  parse_file()

if __name__ == '__main__':
  main()
