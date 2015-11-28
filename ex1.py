def divisibles(quantity, x, y):

	divbyx = []

	divbyy = []

	i = 0

	while len(divbyx) < quantity and len(divbyy) < quantity:

		i+=1

		if i%x == 0:

			divbyx.append(i)

		if i%y == 0:

			divbyy.append(i)

		elif i%x and i%y == 0:

			pass

	print("Found " + str(quantity) + " elements divisible by " + str(x) + " and " + str(y) + " but not both.")

	print("There are " + str(len(divbyx)) + " object in divisible by " + str(x))

	print("There are " + str(len(divbyy)) + " objects in divisible by " + str(y))

	print divbyx

	print divbyy
