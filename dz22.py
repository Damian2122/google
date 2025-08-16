N = 10

def figure_a():
    for i in range(N):
        for j in range(N):
            if j <= N - i - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

def figure_b():
    for i in range(N):
        for j in range(N):
            if j >= i:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

def figure_v():
    for i in range(N):
        for j in range(N):
            if i >= N//2 and abs(j - N//2) <= i - N//2:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

def figure_g():
    for i in range(N):
        for j in range(N):
            if i <= N//2 and abs(j - N//2) <= N//2 - i:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

def figure_d():
    for i in range(N):
        for j in range(N):
            if j >= i and j <= N - i - 1 or j <= i and j >= N - i - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

def figure_e():
    for i in range(N):
        for j in range(N):
            if j <= i and j <= N - i - 1 or j >= i and j >= N - i - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

def figure_zh():
    for i in range(N):
        for j in range(N):
            if j <= i:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

def figure_z():
    for i in range(N):
        for j in range(N):
            if j >= N - i - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

def figure_i():
    for i in range(N):
        for j in range(N):
            if i <= j:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

def figure_k():
    for i in range(N):
        for j in range(N):
            if i >= j:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

def menu():
    while True:
        print("\nФігури: а, б, в, г, д, е, ж, з, и, к")
        print("0 - вихід")
        ch = input("Виберіть фігуру: ")

        if ch == "0":
            break
        elif ch == "а":
            figure_a()
        elif ch == "б":
            figure_b()
        elif ch == "в":
            figure_v()
        elif ch == "г":
            figure_g()
        elif ch == "д":
            figure_d()
        elif ch == "е":
            figure_e()
        elif ch == "ж":
            figure_zh()
        elif ch == "з":
            figure_z()
        elif ch == "и":
            figure_i()
        elif ch == "к":
            figure_k()
        else:
            print("Немає такої фігури!")

menu()
