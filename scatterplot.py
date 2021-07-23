import plotly.express as px
import chart_studio.plotly as py
import plotly.graph_objects as go
import pandas as pd
import numpy as nump
import csv
import plotly as plotly


"""data = pd.read_csv('/Users/haleyrovner/Desktop/ETData43DGraph.csv')
fig = px.scatter_3d(data, x='Place (x)', y='Knowledge (y)', z='Action (z)', color='K5Name', opacity=0.7)

fig.show()"""
knum1 = []
knum2 = []
knum3 = []
knum4 = []
knum5 = []
everything = []

csv1 = open('/Users/haleyrovner/Desktop/knum1.csv', 'w+', newline = '')
csv2 = open('/Users/haleyrovner/Desktop/knum2.csv', 'w+', newline = '')
csv3 = open('/Users/haleyrovner/Desktop/knum3.csv', 'w+', newline = '')
csv4 = open('/Users/haleyrovner/Desktop/knum4.csv', 'w+', newline = '')
csv5 = open('/Users/haleyrovner/Desktop/knum5.csv', 'w+', newline = '')
csvAll = open('/Users/haleyrovner/Desktop/knumAll.csv', 'w+', newline = '')

with open('/Users/haleyrovner/Desktop/ETData43DGraph.csv', 'r') as csvfile:
	datareader = csv.reader(csvfile)
	for x in datareader:
		if(x[4] == '1'):
			knum1.append(x)
		elif(x[4] == '2'):
			knum2.append(x)
		elif(x[4] == '3'):
			knum3.append(x)
		elif(x[4] == '4'):
			knum4.append(x)
		elif(x[4] == '5'):
			knum5.append(x)
		else:
			knum1.append(x)
			knum2.append(x)
			knum3.append(x)
			knum4.append(x)
			knum5.append(x)
		everything.append(x)

with csv1:
	write = csv.writer(csv1)
	write.writerows(knum1)
with csv2:
	write = csv.writer(csv2)
	write.writerows(knum2)
with csv3:
	write = csv.writer(csv3)
	write.writerows(knum3)
with csv4:
	write = csv.writer(csv4)
	write.writerows(knum4)
with csv5:
	write = csv.writer(csv5)
	write.writerows(knum5)
with csvAll:
	write = csv.writer(csvAll)
	write.writerows(everything)

kdata1 = pd.read_csv('/Users/haleyrovner/Desktop/knum1.csv')
kdata2 = pd.read_csv('/Users/haleyrovner/Desktop/knum2.csv')
kdata3 = pd.read_csv('/Users/haleyrovner/Desktop/knum3.csv')
kdata4 = pd.read_csv('/Users/haleyrovner/Desktop/knum4.csv')
kdata5 = pd.read_csv('/Users/haleyrovner/Desktop/knum5.csv')
kdataAll = pd.read_csv('/Users/haleyrovner/Desktop/knumAll.csv')

"""fig1 = px.scatter_3d(kdata1, x='Place (x)', y='Knowledge (y)', z='Action (z)', color='K5Name', opacity=0.7)
fig2 = px.scatter_3d(kdata2, x='Place (x)', y='Knowledge (y)', z='Action (z)', color='K5Name', opacity=0.7)
fig3 = px.scatter_3d(kdata3, x='Place (x)', y='Knowledge (y)', z='Action (z)', color='K5Name', opacity=0.7)
fig4 = px.scatter_3d(kdata4, x='Place (x)', y='Knowledge (y)', z='Action (z)', color='K5Name', opacity=0.7)
fig5 = px.scatter_3d(kdata5, x='Place (x)', y='Knowledge (y)', z='Action (z)', color='K5Name', opacity=0.7)
figAll = px.scatter_3d(kdataAll, x='Place (x)', y='Knowledge (y)', z='Action (z)', color='K5Name', opacity=0.7)"""

fig = go.Figure()
fig.add_trace(
	px.scatter_3d(kdata1, x='Place (x)', y='Knowledge (y)', z='Action (z)', color='K5Name', opacity=0.7))
fig.add_trace(
	px.scatter_3d(kdata2, x='Place (x)', y='Knowledge (y)', z='Action (z)', color='K5Name', opacity=0.7))
fig.add_trace(
	px.scatter_3d(kdata3, x='Place (x)', y='Knowledge (y)', z='Action (z)', color='K5Name', opacity=0.7))
fig.add_trace(
	px.scatter_3d(kdata4, x='Place (x)', y='Knowledge (y)', z='Action (z)', color='K5Name', opacity=0.7))
fig.add_trace(
	px.scatter_3d(kdata5, x='Place (x)', y='Knowledge (y)', z='Action (z)', color='K5Name', opacity=0.7))
fig.add_trace(
	px.scatter_3d(kdataAll, x='Place (x)', y='Knowledge (y)', z='Action (z)', color='K5Name', opacity=0.7))

fig.updatemenus = list([
	dict(type="buttons",
		active=-1,
		showactive=True,
		buttons=list([
			dict(label = 'All Categories',
				method = 'update',
				args=[{"visible": [False, False, False, False, False, True]}]),
			dict(label = 'Ecospirituality',
				method = 'update',
				args=[{"visible": [True, False, False, False, False, False]}]),
			dict(label = 'Small is Beautiful',
				method = 'update',
				args=[{"visible": [False, True, False, False, False, False]}]),
			dict(label = 'Science for Humanity',
				method = 'update',
				args=[{"visible": [False, False, True, False, False, False]}]),
			dict(label = 'Indigenous Justice',
				method = 'update',
				args=[{"visible": [False, False, False, True, False, False]}]),
			dict(label = 'Ecoscience',
				method = 'update',
				args=[{"visible": [False, False, False, False, True, False]}])
			]))])

fig.show()
###print(updatemenus.buttons[0])

###fig1.update_layout(updatemenus=updatemenus)

"""if(fig1.updatemenus.buttons[0] > fig1.updatemenus.buttons[1] and 
	fig1.updatemenus.buttons[0] > fig1.updatemenus.buttons[2] and
	fig1.updatemenus.buttons[0] > fig1.updatemenus.buttons[3] and
	fig1.updatemenus.buttons[0] > fig1.updatemenus.buttons[4] and
	fig1.updatemenus.buttons[0] > fig1.updatemenus.buttons[5]):
	figAll.show()
elif(fig1.updatemenus.buttons[1] > fig1.updatemenus.buttons[0] and 
	fig1.updatemenus.buttons[1] > fig1.updatemenus.buttons[2] and
	fig1.updatemenus.buttons[1] > fig1.updatemenus.buttons[3] and
	fig1.updatemenus.buttons[1] > fig1.updatemenus.buttons[4] and
	fig1.updatemenus.buttons[1] > fig1.updatemenus.buttons[5]):
	fig1.show()
elif(fig1.updatemenus.buttons[2] > fig1.updatemenus.buttons[0] and 
	fig1.updatemenus.buttons[2] > fig1.updatemenus.buttons[1] and
	fig1.updatemenus.buttons[2] > fig1.updatemenus.buttons[3] and
	fig1.updatemenus.buttons[2] > fig1.updatemenus.buttons[4] and
	fig1.updatemenus.buttons[2] > fig1.updatemenus.buttons[5]):
	fig2.show()
elif(fig1.updatemenus.buttons[3] > fig1.updatemenus.buttons[0] and 
	fig1.updatemenus.buttons[3] > fig1.updatemenus.buttons[1] and
	fig1.updatemenus.buttons[3] > fig1.updatemenus.buttons[2] and
	fig1.updatemenus.buttons[3] > fig1.updatemenus.buttons[4] and
	fig1.updatemenus.buttons[3] > fig1.updatemenus.buttons[5]):
	fig3.show()
elif(fig1.updatemenus.buttons[4] > fig1.updatemenus.buttons[0] and 
	fig1.updatemenus.buttons[4] > fig1.updatemenus.buttons[1] and
	fig1.updatemenus.buttons[4] > fig1.updatemenus.buttons[2] and
	fig1.updatemenus.buttons[4] > fig1.updatemenus.buttons[3] and
	fig1.updatemenus.buttons[4] > fig1.updatemenus.buttons[5]):
	fig4.show()
elif(fig1.updatemenus.buttons[5] > fig1.updatemenus.buttons[0] and 
	fig1.updatemenus.buttons[5] > fig1.updatemenus.buttons[1] and
	fig1.updatemenus.buttons[5] > fig1.updatemenus.buttons[2] and
	fig1.updatemenus.buttons[5] > fig1.updatemenus.buttons[3] and
	fig1.updatemenus.buttons[5] > fig1.updatemenus.buttons[4]):
	fig5.show()"""

figAll.show()
