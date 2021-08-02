# import tkinter as tk
# import os
# from time import sleep
#
# input_path = './input/'
# temp = os.scandir(input_path)
# filenames = []
#
# for entry in temp:
#     filenames.append(entry.name)
# filenames.sort()
# all_file_lines = []
# for file in filenames:
#     lines = []
#     temp_in_path = input_path + file
#     with open(temp_in_path) as f:
#         for line in f:
#             if line.rstrip():
#                 data = line.split()
#                 lines.append(data)
#
#         all_file_lines.append(lines)
# i = 0
# while i < len(all_file_lines):
#     del all_file_lines[i][:6]
#     i = i + 1
# tempe = []
# humidty = []
# mesdates = []
# rows = ['Date', 'Temperature', 'Humidity']
# for line in all_file_lines:
#     for l in line:
#         mesdates.append(l[1] + ' ' + l[2])
#         tempe.append(l[3])
#         humidty.append(l[4])




