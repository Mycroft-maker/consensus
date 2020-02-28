import argparse,sys
parse = argparse.ArgumentParser(prog="report",description="a report program",usage='%(prog)s.py [options] -i input_file')
parse.add_argument("-i",help="input file",type=str,required=True)
parse.add_argument("-l",help="left number",type=int,default=15)
parse.add_argument("-r",help="left number",type=int,default=15)
args = parse.parse_args()
label = str()
f1 = open ("{filename}".format(filename=args.i),"r")
info = []
for each_line in f1:
	each_line = each_line.strip()
	if each_line.startswith(">BOP"):
		head = each_line
		label = head.replace(">","")
	elif each_line.startswith(">"):
		continue
	else:
		info.append(each_line)
DATA = []
for a in range(0,len(info[0])):
	linshi = {}
	A_count = 0
	C_count = 0
	G_count = 0
	T_count = 0
	other_count = 0
	for i in info:
		print (a)
                if i[a] == "A":
			A_count += 1
		elif i[a] == "C":
			C_count += 1
		elif i[a] == "G":
			G_count += 1
		elif i[a] == "T":
			T_count += 1
		elif i[a] == "-":
			other_count += 1
	linshi["A"] = A_count
	linshi["C"] = C_count
	linshi["G"] = G_count
	linshi["T"] = T_count
	linshi["-"] = other_count
	DATA.append(linshi)
f3 = open ("{label}.count.xls".format(label=label),"a")
count = 0
for i in DATA:
	count += 1
	info = str()
	info = str(count) + "\t" + str(i["A"]) + "\t" + str(i["T"]) + "\t" + str(i["C"]) + "\t" + str(i["G"]) + "\t"
	first = max(i,key=i.get)
	info = info + str(i[first]) + "\n"
	f3.write(info)

