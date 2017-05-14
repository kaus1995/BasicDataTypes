if __name__ == '__main__':
	print "Enter the dimensions of the cuboid and the value of n"
	x = int(raw_input())
	y = int(raw_input())
	z = int(raw_input())
	n = int(raw_input())
	list = []
	print "Enter the method number to use for comprehensive list i.e 1 or 2"
	num = int(raw_input())
	if num == 1:
		for i in range(x+1):
			for j in range(y+1):
				for k in range(z+1):
					if i+j+k != n:
						coordinate = [i,j,k]
						list.append(coordinate)
					k+=1
				k=0
				j+=1
			j=0
			i+=1
	print list
	elif num == 2:
		coordinate = [[a,b,c] for a in range(x+1) for b in range(y+1) for c in range(z+1) if a+b+c != n]
		print coordinate