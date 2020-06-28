from django.shortcuts import render
from random import randint
from app1.models import dataBase



def index(request):
	
	
	a = randint(1, 94)
	b = randint(1, 94)
	while a==b:
		b - randint(1, 56)
	filepath = "/static/"+str(a)+".jpg"
	filepath2 = "/static/"+str(b)+".jpg"
	args = {
		"a":filepath,
		"b":filepath2
	}

	left = dataBase.objects.get(id=a)
	right = dataBase.objects.get(id=b)
	left.selected = left.selected+1
	right.selected = right.selected+1


	left.save()
	right.save()

	winner_number = 1
	winner =''
	loser=''
	if 'first' in request.POST:
		winner='first'
		winner_number=request.POST['first']
		winner_number=winner_number[winner_number.index('c')+2:winner_number.index('.')]
		loser='second' 
	elif 'second' in request.POST:
		winner='second'
		winner_number=request.POST['second']
		winner_number=winner_number[winner_number.index('c')+2:winner_number.index('.')]
		loser='first'


	winner = dataBase.objects.get(id=winner_number)
	winner.voted=winner.voted+1
	
	winner.save()

		
	return render(request,'home.html',args)

def rankings(request):

	sortedList = []
	data = {}
	for i in range(1, 96):
		item = dataBase.objects.get(id=i)
		if item.selected == 0:
			item.votePer = 0.0
		else:
			item.votePer = item.voted/item.selected
		data[i]=item.votePer
	print(data)
	sortedList = sorted(data.items() , key=lambda t : t[1], reverse=True)
	args = {}
	temp=[]
	for i in sortedList[:10]:
		temp.append(i[0])
	for i in range(len(temp)):
		temp[i]="/static/"+str(temp[i])+".jpg"

	args["data"]=temp	
	print(args)

	return render(request, 'ranking.html', args)
	