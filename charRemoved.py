def equalsWhenOneCharRemoved(x, y):
	res = False
	if equalStrings(x,y)==True:
		res = True
	elif equalStrings(y,x)==True:
		res = True
	return res
	
def equalStrings(x, y):
	for c in range(len(y)):
		s = y[0:c] + y[c+1:]
		if x == s:
			return True
	
	return False
	
'''print(equalsWhenOneCharRemoved("x", "y"))
print(equalsWhenOneCharRemoved("x", "XX"))
print(equalsWhenOneCharRemoved("yy", "yx"))

print(equalsWhenOneCharRemoved("abcd", "abxcd"))
print(equalsWhenOneCharRemoved("xyz", "xz"))'''