x = 0
y = 0
z = 0.5
text = "="
import random
print(text.center(100,"="))
print("""                             Bienvenido

                          Cual es tu nombre?

                              """, end="") 
name = input()
print("""   



""")
print(text.center(100,"="))
print("""
                        Seleccione una Difficultad
      
                               1)Easy
                               2)Normal
                               3)Hard
""")
resp = int(input("                                 "))
print("""


""")
print(text.center(100,"="))
if resp == 1:
      d = 0
      while d < 20:
            r = random.randint(1,2)
            if r == 1:
                  x = random.randint(1,30)
                  y = random.randint(1,30)
                  z = x + y
                  print (" ")
                  print("                          Resuelve:" , x , "+", y)
                  print(" ")
                  ans = int(input("                          Respuesta: "))
                  print("""   

                        """)
                  if ans == z:
                       print(" ")
                       print("                          Correcto :D ")
                       print(text.center(100,"="))
                       d += 1
                  else:
                        print(" ")
                        print("                          Incorrecto D:")
                        print("""   

                       Deseas Continuar? 1)Y 2)N"
                        """)
                        cont = int(input("                       "))
                        print(text.center(100,"="))
                        if cont == 1:
                              d == d
                        else:
                              print("                       Nos vemos pronto")
                              print(text.center(100,"="))
                              exit()
            if r == 2:
                  x = random.randint(1,30)
                  y = random.randint(1,30)
                  z = x - y
                  print(" ")
                  print ("                          Resuelve: ", x, "-", y)
                  print(" ")
                  ans = int(input("                          Respuesta: "))
                  print("""   

                        """)
                  if ans == z:
                        print(" ")
                        print("                          Correcto :D")
                        print(text.center(100,"="))
                        d += 1
                  else:
                        print(" ")
                        print("                          Incorrecto D:")
                        print("""   

                       Deseas Continuar? 1)Y 2)N"
                        """)
                        cont = int(input("                       "))
                        print(text.center(100,"="))
                        if cont == 1:
                              d == d
                        else:
                              print("                       Nos vemos pronto")
                              print(text.center(100,"="))
                              exit()
      print("                          Felicidades :D Respondites todo correcto")
      exit()
if resp == 2:
      d = 0
      while d < 20:
            r = random.randint(1,4)
            if r == 1:
                  x = random.randint(1,30)
                  y = random.randint(1,30)
                  z = x + y
                  print (" ")
                  print("                          Resuelve:" , x , "+", y)
                  print(" ")
                  ans = int(input("                          Respuesta: "))
                  print("""   

                        """)
                  if ans == z:
                       print(" ")
                       print("                          Correcto :D ")
                       print(text.center(100,"="))
                       d += 1
                  else:
                        print(" ")
                        print("                          Incorrecto D:")
                        print("""   

                       Deseas Continuar? 1)Y 2)N"
                        """)
                        cont = int(input("                       "))
                        print(text.center(100,"="))
                        if cont == 1:
                              d == d
                        else:
                              print("                       Nos vemos pronto")
                              print(text.center(100,"="))
                              exit()
            if r == 2:
                  x = random.randint(1,30)
                  y = random.randint(1,30)
                  z = x - y
                  print(" ")
                  print ("                          Resuelve: ", x, "-", y)
                  print(" ")
                  ans = int(input("                          Respuesta: "))
                  print("""   

                        """)
                  if ans == z:
                        print(" ")
                        print("                          Correcto :D")
                        print(text.center(100,"="))
                        d += 1
                  else:
                        print(" ")
                        print("                          Incorrecto D:")
                        print("""   

                       Deseas Continuar? 1)Y 2)N"
                        """)
                        cont = int(input("                       "))
                        print(text.center(100,"="))
                        if cont == 1:
                              d == d
                        else:
                              print("                       Nos vemos pronto")
                              print(text.center(100,"="))
                              exit()
            if r == 3:
                  x = random.randint(1,30)
                  y = random.randint(1,30)
                  z = x * y
                  print(" ")
                  print ("                          Resuelve: ", x, "*", y)
                  print(" ")
                  ans = int(input("                          Respuesta: "))
                  print("""   

                        """)
                  if ans == z:
                        print(" ")
                        print("                          Correcto :D")
                        print(text.center(100,"="))
                        d += 1
                  else:
                        print(" ")
                        print("                          Incorrecto D:")
                        print("""   

                       Deseas Continuar? 1)Y 2)N"
                        """)
                        cont = int(input("                       "))
                        print(text.center(100,"="))
                        if cont == 1:
                              d == d
                        else:
                              print("                       Nos vemos pronto")
                              print(text.center(100,"="))
                              exit()
            if r == 4:
                  x = random.randint(1,30)
                  y = random.randint(1,25)
                  P = x / y
                  z = round(P,1)
                  print(" ")
                  print ("                          Resuelve: ", x, "/", y)
                  print(" ")
                  ans = (input("                          Respuesta: "))
                  print("""   

                        """)
                  if ans == z:
                        print(" ")
                        print("                          Correcto :D")
                        print(text.center(100,"="))
                        d += 1
                  else:
                        print(" ")
                        print("                          Incorrecto D:")
                        print("""   

                       Deseas Continuar? 1)Y 2)N"
                        """)
                        cont = int(input("                       "))
                        print(text.center(100,"="))
                        if cont == 1:
                              d == d
                        else:
                              print("                       Nos vemos pronto")
                              print(text.center(100,"="))
                              exit() 
      print("                          Felicidades :D Respondites todo correcto")     
      exit()               
if resp == 3:
      d = 0
      while d < 20:
            r = random.randint(1,5)
            if r == 1:
                  x = random.randint(1,120)
                  y = random.randint(1,120)
                  z = x + y
                  print (" ")
                  print("                          Resuelve:" , x , "+", y)
                  print(" ")
                  ans = int(input("                          Respuesta: "))
                  print("""   

                        """)
                  if ans == z:
                       print(" ")
                       print("                          Correcto :D ")
                       print(text.center(100,"="))
                       d += 1
                  else:
                        print(" ")
                        print("                          Incorrecto D:")
                        print("""   

                       Deseas Continuar? 1)Y 2)N"
                        """)
                        cont = int(input("                       "))
                        print(text.center(100,"="))
                        if cont == 1:
                              d == d
                        else:
                              print("                       Nos vemos pronto")
                              print(text.center(100,"="))
                              exit()
            if r == 2:
                  x = random.randint(1,120)
                  y = random.randint(1,120)
                  z = x - y
                  print(" ")
                  print ("                          Resuelve: ", x, "-", y)
                  print(" ")
                  ans = int(input("                          Respuesta: "))
                  print("""   

                        """)
                  if ans == z:
                        print(" ")
                        print("                          Correcto :D")
                        print(text.center(100,"="))
                        d += 1
                  else:
                        print(" ")
                        print("                          Incorrecto D:")
                        print("""   

                       Deseas Continuar? 1)Y 2)N"
                        """)
                        cont = int(input("                       "))
                        print(text.center(100,"="))
                        if cont == 1:
                              d == d
                        else:
                              print("                       Nos vemos pronto")
                              print(text.center(100,"="))
                              exit()
            if r == 3:
                  x = random.randint(1,40)
                  y = random.randint(1,40)
                  z = x * y
                  print(" ")
                  print ("                          Resuelve: ", x, "*", y)
                  print(" ")
                  ans = int(input("                          Respuesta: "))
                  print("""   

                        """)
                  if ans == z:
                        print(" ")
                        print("                          Correcto :D")
                        print(text.center(100,"="))
                        d += 1
                  else:
                        print(" ")
                        print("                          Incorrecto D:")
                        print("""   

                       Deseas Continuar? 1)Y 2)N"
                        """)
                        cont = int(input("                       "))
                        print(text.center(100,"="))
                        if cont == 1:
                              d == d
                        else:
                              print("                       Nos vemos pronto")
                              print(text.center(100,"="))
                              exit()
            if r == 4:
                  x = random.randint(1,30)
                  y = random.randint(1,25)
                  P = x / y
                  z = round(P,1)
                  print(" ")
                  print ("                          Resuelve: ", x, "/", y)
                  print(" ")
                  ans = float(input("      (Aproxima 1 decimal) Respuesta: "))
                  print("""   

                        """)
                  if ans == z:
                        print(" ")
                        print("                          Correcto :D")
                        print(text.center(100,"="))
                        d += 1
                  else:
                        print(" ")
                        print("                          Incorrecto D:")
                        print("""   

                       Deseas Continuar? 1)Y 2)N"
                        """)
                        cont = int(input("                       "))
                        print(text.center(100,"="))
                        if cont == 1:
                              d == d
                        else:
                              print("                       Nos vemos pronto")
                              print(text.center(100,"="))
                              exit()
            if r == 5:
                  x = random.randint(1,10)
                  y = random.randint(1,4)
                  z = x**y
                  print(" ")
                  print ("                          Resuelve: ", x, "^", y)
                  print(" ")
                  ans = int(input("                          Respuesta: "))
                  print("""   

                        """)
                  if ans == z:
                        print(" ")
                        print("                          Correcto :D")
                        print(text.center(100,"="))
                        d += 1
                  else:
                        print(" ")
                        print("                          Incorrecto D:")
                        print("""   

                       Deseas Continuar? 1)Y 2)N"
                        """)
                        cont = int(input("                       "))
                        print(text.center(100,"="))
                        if cont == 1:
                              d == d
                        else:
                              print("                       Nos vemos pronto")
                              print(text.center(100,"="))
                              exit()    
      print("                          Felicidades :D Respondites todo correcto") 
