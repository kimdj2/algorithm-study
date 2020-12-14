def main():
  a=1
  b=2

  max_val = max(a, b)
  print(f"{max_val}")

def max(a :int, b :int):
  """
  max function
  """
  if a < b:
    return b
  else:
    return a

if __name__ == '__main__':
    main()
    