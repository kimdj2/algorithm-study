def main():
  a = [5,3,2,1,4]
  min_val = float('inf')

  for i in a:
    if i < min_val:
      min_val = i

  print(min_val)


if __name__ == '__main__':
    main()