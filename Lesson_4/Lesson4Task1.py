import sys

path, zarplata, stavka, premia = sys.argv
print(sys.argv)
print((int(zarplata) * int(stavka)) + int(premia))
