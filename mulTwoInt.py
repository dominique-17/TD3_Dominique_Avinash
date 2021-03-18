import sys

def mul():
	x = int( sys.argv[1] )
	y = int( sys.argv[2] )

	if len(sys.argv) >= 4:
		message = "you have added more than 2 args"
		print(message)
	
	if len(sys.argv) < 3:
		msg = "You have less than 2 args"
		print(msg)

	if len(sys.argv) == 3:
		print(x * y)

mul()
