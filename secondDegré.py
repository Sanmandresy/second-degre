import math
#2nd degré
a = int(input("Donnez une valeur de a : "))
b = int(input("Donnez une valeur de b : "))
c = int(input("Donnez une valeur de c : "))
if a == 0 and b == 0:
     print("Ce n'est pas une équation du second degré !")
elif a == 0 and b != 0:
    print("Ce n'est pas une équation du second degré ! C'est plutôt une équation du premier degré avec comme solution x = {} ".format(-c/b))
elif a != 0:
    choice = input("Utiliser b ou b' ? ")
    if choice == "b":
          if b % 2 != 0:
               print("Vous avez une équation du second degré de la forme " + str(a) + "x² + " + str(b) + "x + " + str(c))
               delta = ( (b*b)-4*(a*c) )
               print("Vous avez delta(d) = {} ".format(delta))
               if delta == 0:
                    x = -b/2*a
                    print("Vous avez comme solution x1 = x2 = " + str(x))
               elif delta < 0:
                    print("Vous n'avez pas de solution !")
               elif delta > 0:
                    racine_de_delta = math.sqrt(delta)
                    x1 = (-b - racine_de_delta)/2*a            
                    x2 = (-b + racine_de_delta)/2*a
                    print(" Vous avez comme solution x1 = {} et x2 = {} ".format(x1,x2))
          else:
               print("utiliser b'")
    elif choice == "b'":
        if b % 2 != 0:
               print("Utiliser b")
        else:
             print("Vous avez une équation du second degré de la forme " + str(a) + "x² + " + str(b) + "x + " + str(c))
             bp = b/2
             delta_prime = ( (bp)**2 -(a*c) )
             print("Vous avez delta_prime(d') = {} ".format(delta_prime))
             if delta_prime == 0:
                    x = -bp/a
                    print("Vous avez comme solution x1 = x2 = " + str(x))
             elif delta_prime < 0:
                    print("Vous n'avez pas de solution !")
             elif delta_prime > 0:
                    racine_de_delta = math.sqrt(delta_prime)
                    x1 = (-bp - racine_de_delta)/a            
                    x2 = (-bp + racine_de_delta)/a
                    print(" Vous avez comme solution x1 = {} et x2 = {} ".format(x1,x2))
