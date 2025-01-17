import pandas as pd
import dash
from dash import dcc, html
import plotly.express as px
import datetime

# Example data
timestamps = [1609459200, 1609459260, 1609459320]  # logMonoTime timestamps in seconds
events = ['Event 1', 'Event 2', 'Event 3']
categories = ['Category A', 'Category B', 'Category A']

# Convert timestamps to datetime
dates = [datetime.datetime.fromtimestamp(ts) for ts in timestamps]

# Create a DataFrame
data = {'Timestamp': dates, 'Event': events, 'Category': categories}
df = pd.DataFrame(data)

# Create a scatter plot with categories
fig = px.scatter(df, x='Timestamp', y='Event', color='Category', title='Interactive Timeline with Categories')

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout of the app
app.layout = html.Div([
    html.H1('Interactive Timeline'),
    dcc.Graph(
        id='timeline-plot',
        figure=fig
    )
])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
