from pandas_datareader import data
import datetime
from bokeh.plotting import figure, show, output_file

timeStart = datetime.datetime(2016, 3, 1)
timeEnd = datetime.datetime(2019, 10, 31)
df = data.DataReader(name='GOOG', data_source = 'yahoo', start=timeStart, end=timeEnd)

def candleSticks(top, bottom):
    if top > bottom:
        value = 'Increase'
    elif top < bottom:
        value = 'Decrease'
    else:
        value = 'Equal'
    return value

df['Status'] = [candleSticks(top, bottom) for top, bottom in zip(df.Close, df.Open)]
df['Middle'] = (df.Open+df.Close)/2
df['Height'] = abs(df.Close-df.Open)

print(df)

pandas = figure(x_axis_type='datetime', width = 200, height = 100, sizing_mode = 'scale_width')
pandas.title.text = 'Candle Stick Stock'
pandas.grid.grid_line_alpha = 0.3

hours_12 = 12*60*60*1000

pandas.segment(df.index, df.High, df.index, df.Low, color='black')

pandas.rect(df.index[df.Status == 'Increase'], df.Middle[df.Status == 'Increase'], hours_12, df.Height[df.Status == 'Increase'], fill_color='green', line_color='black')
pandas.rect(df.index[df.Status == 'Decrease'], df.Middle[df.Status == 'Decrease'], hours_12, df.Height[df.Status == 'Decrease'], fill_color='red', line_color='black')

output_file('CS.html')
show(pandas)


