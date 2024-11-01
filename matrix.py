N = 3
def ab(mat, n):
	sum = 0
	for i in range(n):
		sum += mat[i][i]
	return sum
def s(mat, n):
	return ((mat[2][2] * mat[1][1] - mat[2][1] * mat[1][2])
	+ (mat[2][2] * mat[0][0] - mat[2][0] * mat[0][2])
	+ (mat[1][1] * mat[0][0] - mat[1][0] * mat[0][1]))
def dd(mat, b, p, q, n):
	i,j = 0,0
	for row in range(n):
		for col in range(n):
			if (row != p and col != q):
					b[i][j] = mat[row][col]
					j += 1
					if (j == n - 1):
						j = 0
						i += 1
def dm(mat, n):
	D = 0
	if (n == 1):
		return mat[0][0]
	b = [[0 for i in range(n)] for j in range(n)]
	s = 1
	for f in range(n):
		dd(mat, b, 0, f, n)
		D += s * mat[0][f] * dm(b, n - 1)
		s = -s
	return D
mat = [[3, 4, 5], [6, 0, -1], [2, -1, 0]]
t = ab(mat, 3)
c = s(mat, 3)
det = dm(mat, 3)
print("x^3",end="")
if (t != 0):
	print(f" {t * -1}x^2",end="") if(t < 0) else print(f" - {t}x^2",end="")
if (c != 0):
	print(f" - {c * -1}x",end="") if(c < 0) else print(f" + {c}x",end="")
if (det != 0):
	print(f" + {det * -1}",end="") if (det < 0) else print(f" - {det}",end="")

