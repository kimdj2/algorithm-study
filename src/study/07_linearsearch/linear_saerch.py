def main():
  a = [5,3,2,1,4]
  print(linear_search(a, 2))

def linear_search(a, key):
  for i in range(len(a)):
    if i == key:
      return i
  return None

if __name__ == '__main__':
    main()