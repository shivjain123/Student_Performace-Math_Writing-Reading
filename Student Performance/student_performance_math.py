import csv
import plotly.figure_factory as pff
import statistics as s
import plotly.graph_objects as go

with open("D:/(4) WhiteHatJr. Codes/Third Module/Normal Distribution/Project/Student Performance/Students_Performance.csv", newline="") as f:
    reader = list(csv.reader(f))
    reader.pop(0)

    performance_list_math = []

    for i in range(len(reader)):
        math = reader[i][5]
        performance_list_math.append(float(math))

len_list = len(performance_list_math)

total = 0

for t in performance_list_math:
    total += t

mean = total/len_list

print()
print("The Mean is " + str(mean) + ".")

mode_of_list = s.mode(performance_list_math)

median_of_list = s.median(performance_list_math)

devaition = s.stdev(performance_list_math)

d_1_left, d_1_right = mean - devaition, mean + devaition

d_2_left, d_2_right = mean - (devaition*2), mean + (devaition*2)

d_3_left, d_3_right = mean - (devaition*3), mean + (devaition*3)

r_list_first = [r for r in performance_list_math if (r > d_1_left and r < d_1_right)]

percent_first_sd = len(r_list_first)/len(performance_list_math) * 100

r_list_second = [r for r in performance_list_math if(r > d_2_left and r < d_2_right)]

percent_second_sd = len(r_list_second)/len(performance_list_math) * 100

print()
print("The Mode is", mode_of_list)
print()
print("The Median is ", median_of_list)
print()
print("The Standard Deviation is ", devaition)
print()
print(percent_first_sd, "% of data lies in the first deviation.")
print()
print(percent_second_sd, "% of data lies in the second deviation.")
print()

figure = pff.create_distplot([performance_list_math], ["Results"], show_hist=False)

figure.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.03], mode="lines", name="mean"))

figure.add_trace(go.Scatter(x=[d_1_left, d_1_left], y=[0, 0.03], mode="lines", name="First Standard Deviation (Start)"))
figure.add_trace(go.Scatter(x=[d_1_right, d_1_right], y=[0, 0.03], mode="lines", name="First Standard Deviation (End)"))

figure.add_trace(go.Scatter(x=[d_2_left, d_2_left], y=[0, 0.03], mode="lines", name="Second Standard Deviation (Start)"))
figure.add_trace(go.Scatter(x=[d_2_right, d_2_right], y=[0, 0.03], mode="lines", name="Second Standard Deviation (End)"))

figure.show()