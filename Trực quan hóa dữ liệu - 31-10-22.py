import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
x_ = [2,4,6,8,10]
y_ = [12.2,16.3,20.5,25.4,31.2]
data = pd.DataFrame()
data.loc[:,"x"] = pd.DataFrame(x_)
data.loc[:,"y"] = pd.DataFrame(y_)
data
#vẽ y theo x
plt.plot(data.loc[:,"x"], data.loc[:,"y"], label = "Ví dụ") #plot vẽ biểu đồ đường, nếu label = "_ ví dụ" khi có _ label sẽ ko hiển thị
plt.title("Đồ thị y theo X", fontdict={"fontsize": 18,
                                       "fontweight": 20,
                                       "color": "blue",
                                       "verticalalignment" : "baseline",
                                       "horizontalalignment" : "center"})
#horizontalalignment căn giữa
#verticalalignment căn sát
plt.xlabel("Trục X", loc = "left", fontdict={"color": "blue",
                                       "horizontalalignment" : "center"})
plt.ylabel("Trục y", fontdict={"color": "red",
                                       "horizontalalignment" : "center"})
plt.legend() #hiển thị label = "ví dụ"
#loc (location) mặc định là center, đối với trục X : left, right
#đối với trục y: top, bottom
#thay đổi cài đặ Axes, Axis
plt.plot(data.loc[:,"x"], data.loc[:,"y"])
axes1 = plt.gca() # chỉ lấy khung của plt
                                       

