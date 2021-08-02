import sys
import xlsxwriter
import plotly
import plotly.graph_objects as go
import pandas as pd
import os
import tkinter as tk
from random import randint

value = randint(0, 1000)

def fun(randnum):
    videos = ['https://www.youtube.com/watch?v=fHhKIZTLUYY','https://www.youtube.com/watch?v=woOiVm5_FwI', ]
    if randnum == 7:
        tempfil = open('HeyHeyHeyBeniIzle.txt', 'w')
        tempfil.write(videos[0])
        tempfil.close()
    if randnum == 19:
        tempfil = open('HeyHeyHeyBeniIzle.txt', 'w')
        tempfil.write(videos[1])
        tempfil.close()

def partial_reporter():
    error = ''

    input_path = './input/'
    output_path = './output/'

    cond1 = os.path.isdir(input_path)
    cond2 = os.path.isdir(output_path)

    if cond1 is False:
        os.mkdir(input_path)
    if cond2 is False:
        os.mkdir(output_path)

    cond3 = os.listdir(input_path)

    if len(cond3) == 0:
        error = 'Input dosyasi bos!!!'


    with os.scandir(input_path) as entries:
        for entry in entries:
            lines = []
            temp_in_path = input_path + entry.name
            with open(temp_in_path) as f:
                for line in f:
                    if line.rstrip():
                        data = line.split()
                        lines.append(data)
            f.close()
            del lines[:6]
            tempe = []
            humidty = []
            mesdates = []
            rows = ['Date', 'Temperature', 'Humidity']
            # convert list system into
            for line in lines:
                mesdates.append(line[1] + ' ' + line[2])
                tempe.append(line[3])
                humidty.append(line[4])
            workbook = xlsxwriter.Workbook(f'{entry.name}')
            worksheet = workbook.add_worksheet()
            worksheet.write_row('A1', rows)
            worksheet.write_column('A2', mesdates)
            worksheet.write_column('B2', tempe)
            worksheet.write_column('C2', humidty)
            workbook.close()

            excel_file = f'{entry.name}'
            df = pd.read_excel(excel_file)
            outname = entry.name
            modoutname = outname.replace('.txt', '')

            fig = go.Figure()
            fig.add_trace(go.Scatter(x=df['Date'], y=df['Humidity'], name='Humidity', line = dict(color='blue', width=4)))
            fig.add_hline(y=20)
            fig.add_hline(y=80)
            # fig.update_traces(hoverinfo='text+name', mode='lines+markers')
            # fig.update_layout(legend=dict(y=0.5, traceorder='reversed', font_size=16))
            temp_out_path = output_path + modoutname + '-Humidity' + '.html'
            plotly.offline.plot(fig, filename=temp_out_path)

            os.remove(f'{entry.name}')

            fig2 = go.Figure()
            fig2.add_trace(go.Scatter(x=df['Date'], y=df['Temperature'], name='Temperature', line = dict(color='firebrick', width=4)))
            fig2.add_hline(y=18)
            fig2.add_hline(y=28)
            anan = output_path + modoutname + '-Temperature' + '.html'
            plotly.offline.plot(fig2, filename=anan)

    if error is not None:
        tempfil = open('ErrorLogs.txt', 'w')
        tempfil.write(error)
        tempfil.close()

    fun(value)

def all_reporter():
    error = ''
    input_path = './input/'
    output_path = './output/'

    cond1 = os.path.isdir(input_path)
    cond2 = os.path.isdir(output_path)

    if cond1 is False:
        os.mkdir(input_path)
    if cond2 is False:
        os.mkdir(output_path)

    cond3 = os.listdir(input_path)

    if len(cond3) == 0:
        error = 'Input dosyasi bos!!!'

    temp = os.scandir(input_path)
    filenames = []

    for entry in temp:
        filenames.append(entry.name)
    filenames.sort()
    all_file_lines = []
    for file in filenames:
        lines = []
        temp_in_path = input_path + file
        with open(temp_in_path) as f:
            for line in f:
                if line.rstrip():
                    data = line.split()
                    lines.append(data)

            all_file_lines.append(lines)
    i = 0
    while i < len(all_file_lines):
        del all_file_lines[i][:6]
        i = i + 1
    tempe = []
    humidty = []
    mesdates = []
    rows = ['Date', 'Temperature', 'Humidity']
    for line in all_file_lines:
        for l in line:
            mesdates.append(l[1] + ' ' + l[2])
            tempe.append(l[3])
            humidty.append(l[4])
    workbook = xlsxwriter.Workbook(f'{entry.name}')
    worksheet = workbook.add_worksheet()
    worksheet.write_row('A1', rows)
    worksheet.write_column('A2', mesdates)
    worksheet.write_column('B2', tempe)
    worksheet.write_column('C2', humidty)
    workbook.close()
    excel_file = f'{entry.name}'
    df = pd.read_excel(excel_file)
    outname = entry.name
    modoutname = outname.replace('.txt', '')

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df['Date'], y=df['Humidity'], name='Humidity', line=dict(color='blue', width=4)))
    fig.add_hline(y=20)
    fig.add_hline(y=80)
    # fig.update_traces(hoverinfo='text+name', mode='lines+markers')
    # fig.update_layout(legend=dict(y=0.5, traceorder='reversed', font_size=16))
    temp_out_path = output_path + modoutname + '-Humidity' + '.html'
    plotly.offline.plot(fig, filename=temp_out_path)

    os.remove(f'{entry.name}')

    fig2 = go.Figure()
    fig2.add_trace(go.Scatter(x=df['Date'], y=df['Temperature'], name='Temperature', line=dict(color='firebrick', width=4)))
    fig2.add_hline(y=18)
    fig2.add_hline(y=28)
    anan = output_path + modoutname + '-Temperature' + '.html'
    plotly.offline.plot(fig2, filename=anan)

    if error is not None:
        tempfil = open('ErrorLogs.txt', 'w')
        tempfil.write(error)
        tempfil.close()
    fun(value)


root = tk.Tk()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="All Report", command=all_reporter)
button2 = tk.Button(root, text="Seperate Report", command=partial_reporter)

button2.pack()
button.pack()

root.mainloop()
