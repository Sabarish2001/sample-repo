def cal_pos(Genome,pattern):
	pos_list = []
	g = len(Genome)
	p = len(pattern)
	
	for n  in range(g - p  + 1 ):
		if Genome[i : i + p] == pattern:
			pos_list.append(i)
	return pos_list
	

