import plotly.graph_objs as go
import plotly.plotly as py
import numpy as np
import plotly 
import cPickle

plotly.tools.set_credentials_file(username='JerryYanWan', api_key= 'hw5T5JtiXDvPoEurJwja') 

# Creating the data
data = cPickle.load(open("/Users/ywan/Documents/myGithub/MCM/data.pkl", "rb"))
[x, y, z] = data
x = np.array(x)
y = np.array(y)
z = np.array(z)
# x = np.linspace(-5, 5, 50)
# y = np.linspace(-5, 5, 50)
xGrid, yGrid = np.meshgrid(x, y)
# R = np.sqrt(xGrid ** 2 + yGrid ** 2)
# z = np.sin(R)

# Creating the plot
#lines = []
#line_marker = dict(color='#0066FF', width=2)
#for i, j, k in zip(xGrid, yGrid, z):
#    lines.append(go.Scatter3d(x=i, y=j, z=k, mode='lines', line=line_marker))
#
layout = go.Layout(
    title='network flow data simulation for Zone B',
    scene=dict(
        xaxis=dict(
            gridcolor='rgb(255, 255, 255)',
            zerolinecolor='rgb(255, 255, 255)',
            showbackground=True,
            backgroundcolor='rgb(230, 230,230)'
        ),
        yaxis=dict(
            gridcolor='rgb(255, 255, 255)',
            zerolinecolor='rgb(255, 255, 255)',
            showbackground=True,
            backgroundcolor='rgb(230, 230,230)'
        ),
        zaxis=dict(
            gridcolor='rgb(255, 255, 255)',
            zerolinecolor='rgb(255, 255, 255)',
            showbackground=True,
            backgroundcolor='rgb(230, 230,230)'
        )
    ),
    xaxis = go.XAxis(
      title = 'p_1'
    ),
    yaxis = go.YAxis(
      title = 'p_2'
    ),
    showlegend=False
)
# trace1 = go.Surface(z = z, colorscale='Viridis')
trace = go.Mesh3d(x=x, y=y, z=z, color = '91EE90', opacity=0.75)
goData = go.Data([trace])
fig = go.Figure(data = goData, layout = layout)
py.iplot(fig, filename = 'lpsimulation')
#fig = go.Figure(data=lines, layout=layout)
#py.iplot(fig, filename='lpsimulation')
