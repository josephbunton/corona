import numpy as np
from scipy.optimize import curve_fit
import plotly.graph_objects as go

x = np.array(range(58))
y = np.array(
    [3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 6, 6, 13,
     22, 22, 26, 28, 38, 48, 55, 65, 65, 92, 112, 134, 171, 210, 267, 307, 353, 436, 533, 533])

# make the plot!
fig = go.Figure()
# The original function
fig.add_trace(go.Scatter(x=x, y=y, mode='markers', name='Actual'))
fig.update_layout(title='First 57 days corona virus totals NSW',
                  xaxis_title='Days since first case',
                  yaxis_title='Number of cases')
#fig.show()

fit_58 = curve_fit(lambda t, a, b: a * np.exp(b * t), x[:-1], y[:-1], p0=(4, 0.1))
fit_59 = curve_fit(lambda t, a, b: a * np.exp(b * t), x, y, p0=(4, 0.1))

x_pred = np.array(range(65))

y_fit_58 = [fit_58[0][0]*np.exp(fit_58[0][1]*t) for t in x_pred]
y_fit_59 = [fit_59[0][0]*np.exp(fit_59[0][1]*t) for t in x_pred]

fig.add_trace(go.Scatter(x=x_pred, y=y_fit_58, mode='lines', name='Exponential Fit (First 58 Days)'))
fig.add_trace(go.Scatter(x=x_pred, y=y_fit_59, mode='lines', name='Exponential Fit (First 59 Days)'))

fig.show()
