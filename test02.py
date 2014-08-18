#encoding:utf-8
i = 2
while (i < 100):
	j = 2
	while (j <= (i / j)):
		if not (i % j): break
		j = j + 1
	if (j > i / j): print i ,"是素数".decode('utf-8','ignore')
	i = i + 1
print "good"