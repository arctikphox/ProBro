print("MathHomework.py")
problem = input("Enter a math problem, or 'q' quit:")
while (problem != "q"):
	print("The answer to ", problem, "is:", eval(problem) )
	problem = input("Enter another math problem, or 'q' to quit: ")
	#1'q' to quit
