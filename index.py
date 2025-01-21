import pandas as pd
import matplotlib.pyplot as plt

salida = plt.subplot()
entrada = pd.DataFrame(pd.read_csv("avocado.csv"))

# print(entrada["region"].to_string())

Sacramento = entrada[entrada["region"] == "Sacramento"]
Southeast = entrada[entrada["region"] == "Southeast"]
Mexico = entrada[entrada["region"] == "WestTexNewMexico"]

g_Sacramento = Sacramento.plot(x = "year" , y = "AveragePrice" , kind = "scatter" , color = "red" , ax = salida)
g_Tampa = Southeast.plot(x = "year" , y = "AveragePrice" , kind = "scatter" , color = "green" , ax = salida)
g_Miami = Mexico.plot(x = "year" , y = "AveragePrice" , kind = "scatter" , color = "blue" , ax = salida)

plt.show()