class chartjs:
    def __init__(self):
        self.backgroundColors = {
            "blue": "rgba(86, 150, 212, 0.4)",
            "yellow": "rgba(252, 207, 38, 0.4)",
            "green": "rgba(123, 202, 165, 0.4)",
            "red": "rgba(235, 117, 101, 0.4)",
            "purple": "rgba(162, 96, 170, 0.4)"
            }
        self.borderColors = {
            "blue": "rgba(86, 150, 212, 1)",
            "yellow": "rgba(252, 207, 38, 1)",
            "green": "rgba(123, 202, 165, 1)",
            "red": "rgba(235, 117, 101, 1)",
            "purple": "rgba(162, 96, 170, 1)"
            }
        self.response = {"labels": [], "datasets": [], "length": 0}
        self.dataset = {
            "fill": 0,
            "lineTension": 0.1,
            "borderCapStyle": 'butt',
            "borderDash": [],
            "borderDashOffset": 0.0,
            "borderJoinStyle": 'miter',
            "pointBackgroundColor": "#fff",
            "pointBorderWidth": 1,
            "pointHoverRadius": 3,
            "pointHoverBorderWidth": 2,
            "pointRadius": 1,
            "pointHitRadius": 10,
            "spanGaps": "false"
            }

    def addDataset(self, label, data, color, **kwargs):
        self.dataset["label"] = label
        self.dataset["data"] = data
        self.dataset["backgroundColor"] = self.backgroundColors[color]
        self.dataset["pointHoverBackgroundColor"] = self.backgroundColors[color]
        self.dataset["borderColor"] = self.borderColors[color]
        self.dataset["pointBorderColor"] = self.borderColors[color]
        self.dataset["pointHoverBorderColor"] = self.borderColors[color]

        for key in kwargs:
            self.dataset[key] = kwargs[key]

        self.response["datasets"].append(self.dataset)
        self.dataset = {
            "fill": 0,
            "lineTension": 0.1,
            "borderCapStyle": 'butt',
            "borderDash": [],
            "borderDashOffset": 0.0,
            "borderJoinStyle": 'miter',
            "pointBackgroundColor": "#fff",
            "pointBorderWidth": 1,
            "pointHoverRadius": 3,
            "pointHoverBorderWidth": 2,
            "pointRadius": 1,
            "pointHitRadius": 10,
            "spanGaps": "false"
            }

    def addLabels(self, labels):
        self.response["labels"] = labels
