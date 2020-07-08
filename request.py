# import json
# file = open('request.json','r')
# a=file.read()
# file.close()
# # print(a)
# b=json.loads(a)
# # print(b)
# for i in b.values():
# 	# print(i)
# 	for j in i:
# 		# print(j)
# 		for x in j:
# 			pass
# 		print(j['id'])


# import requests,json
# r = requests.get('http://saral.navgurukul.org/api/courses')
# with open('request.json','w+') as i:
# 	c=json.dump(r.text,i)
# 	c=json.loads(r.text)
# 	empty={}
# 	for i in c.values():
# 		for j in range(len(i)):
# 			# print(j)
# 			e=(j+1,i[j]['id'])
# 			empty[j+1]=i[j]['id']
# a=int(input('enter no.  '))
# for x in empty.keys():
# 	if a==x:
# 		print(empty[a])


# file = open('request.json','w')
# file.write(b)
# file.close()
# import json

# file = open('request.json','r')
# a = file.read()
# file.close()
# # print(a)
# b=json.loads(a)
# for i in b.values():
# 	# print(i)
# 	for j in i:
# 		for x in j:
# 			pass
# 		print(j['id'])


# import requests
# import json,os
# while True:
# 	print('Loading......')
	# r = requests.get('http://saral.navgurukul.org/api/courses')
	# # print(r)

	# with open('request.json','w+') as i:
	# 	c=json.dump(r.text,i)
	# 	c=json.loads(r.text)
# 		for i in c.values():
# 			for j in range(len(i)):
# 				if j<9:
# 					k='0'+str(j+1)
# 					print(k+'. ',i[j]['id'],' ','Name - ',i[j]['name'])
# 				else:
# 					print(str(j+1)+'. ',i[j]['id'],' ','Name - ',i[j]['name'])
# 	j=int(input('enter no.  '))
# 	print('Loading.....')
# 	print(str(j)+'. ',i[j-1]['id'],' ','Name - ',i[j-1]['name'])
# 	k=i[j-1]['id']

# 	while True:
# 		f = requests.get('http://saral.navgurukul.org/api/courses/'+str(k)+'/exercises')
# 		# print(f)
# 		with open('request.json','w+') as n:
# 			c=json.dump(f.text,n)
# 			c=json.loads(f.text)
# 			for i in c.values():
# 				for j in range(len(i)): 
# 					# print(j)
# 					if j<9:
# 						x='0'+str(j+1)
# 						print('       ',x+'. ',' ','Name - ',i[j]['name'])
# 					else:
# 						print('       ',str(j+1)+'. ',' ','Name - ',i[j]['name'])
# 		ask=input('''
# 				** you want to:-
# 				1. courses then press ("c")
# 				2. Next page          ("n")
# 				3. Previous page      ("p")\n:- 
# 		:-''')
# 		if ask=='c':
# 			break
# 		elif k<14 and k>92:
# 			k==14
# 			print('Previous page is not available')
# 		elif(ask=='p'):
# 			(k)-=1
# 		elif(ask=='n'):
# 			(k)+=1
		
# 		elif k<14 and k>92:
# 			k==14
# 			print('Previous page is not available')
# 		else:
# 			k=92
# 			print('next page is not available')
# 			print('id-',k)
# 	last=input('you want to exit. PRESS-EXIT\n').lower()
# 	if 'exit'.lower() == last:
# 		break
		



