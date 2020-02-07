def stringConvertion():
  user = input("Enter your string: \n")
  print(''' 
  Your input: {}\n
      +-----------------------------------------+
      | input   hex\t oct \t dec \t  bin\t|
      +-----------------------------------------+
    '''.format(user))
  for i in range(len(user)):
    char = user[i]
    if char != " ":
      for x in char:
        hexa = "".join(format(ord(x), "x"))
        octa = "".join(format(ord(x), "o"))
        deci = "".join(format(ord(x), "d"))
        bin = "".join(format(ord(x), "b"))
        print("\t",char, "\t", hexa, "\t", octa, "\t", deci, "\t", bin)  
    else:
      print()
stringConvertion()
