import numpy as np 


def function(x):
    return x**3 + 8
def main():
	result = function(9)
	print(result)
	if result > 27:
		print ("YAY!")
if __name__ == "__main__":
    main()

