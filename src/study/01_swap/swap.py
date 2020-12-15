def main():
  a = 1
  b = 2
  a, b = swap(a,b)
  print(f"a:{a} b:{b}")

def swap(a :int, b: int):
  t = a
  a = b
  b = t
  
  return a, b
    
if __name__ == '__main__':
    main()