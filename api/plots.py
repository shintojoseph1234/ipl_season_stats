from plotly.offline import plot
import plotly.graph_objs as go

def bar_graph(x,y,heading='',colors=[]):

    data=[]

    trace =go.Bar(
                x=x,
                y=y,
                marker_color=colors,
            )

    layout = go.Layout(
                title=heading,
                height=400,
                width=800,
                xaxis=dict(
                    autorange=True
                ),
                yaxis=dict(
                    autorange=True
                )
            )

    data.append(trace)

    fig = go.Figure(data=data, layout=layout)

    fig.update_xaxes(showgrid=False, zeroline=False)
    fig.update_yaxes(showgrid=False, zeroline=False)

    plot_div = plot(fig, output_type='div', include_plotlyjs=False, config={"displayModeBar": False})

    return plot_div


def pie_graph(labels,values,colors):

    data = []

    trace = go.Pie(
                    labels=labels,
                    values=values
                  )
    data.append(trace)

    layout = go.Layout(
                height=400,
                width=400,
            )

    fig = go.Figure(data=data, layout=layout)

    fig.update_traces(hoverinfo='label+percent',
                      textinfo='label',
                      textfont_size=15,
                      marker=dict(colors=colors)
                     )

    plot_div = plot(fig, output_type='div', include_plotlyjs=False, config={"displayModeBar": False})

    return plot_div



def bar_graph_data_cleaner(data):
    '''
    clean the data for graph
    '''

    x = list(data.keys())
    y = list(data.values())

    max_key = max(data, key=data.get)

    colors = ["crimson" if each==max_key else "lightslategray" for each in data]

    return x,y,colors


def pie_graph_data_cleaner(data):
    '''
    clean the data for graph
    '''
    labels = list(data.keys())
    values = list(data.values())

    colors = ["crimson" if each=="BAT" else "lightslategray" for each in data]

    return labels,values,colors
