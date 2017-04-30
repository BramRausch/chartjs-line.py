# chartjs-line.py
Python module to generate chartjs-line JSON data

## usage
``` Python
addDataset(label, data, color, **kwargs)
```
  * label: The title of the dataset (str)
  * data: A list of data
  * color: One of the build in colors (blue, yellow, green, red, purple)
  * **kwargs: Additional chartJS settings

``` Python
addLabels(labels)
```
  * labels: List of labels


## Example:
``` Python
import chartjs
chart = chartjs.chartjs()

chart.addDataset("Temperature", [20, 20, 21, 20], "blue", borderDash=[0, 1])  # Dashed line
chart.addDataset("Humidity", [30, 31, 29, 30], "yellow")
chart.addLabels(["10:00", "11:00", "12:00", "13:00"])

chart.response
```

Open example.html to see the chart rendered
