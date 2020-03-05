import React from "react";
import FusionCharts from "fusioncharts";
import charts from "fusioncharts/fusioncharts.charts";
import ReactFusioncharts from "react-fusioncharts";

// Resolves charts dependancy
charts(FusionCharts);

const dataSource = {
  "chart": {
    "xAxisName": "Products/Services",
    "yAxisName": "Markets",
    "numberSuffix": "",
    "theme": "fusion"
  },
  "data": [
    {
      "value": "290"
    },
    {
      "value": "260"
    },
    {
      "value": "180"
    },
    {
      "value": "140"
    },
    {
      "value": "115"
    },
    {
      "value": "100"
    },
    {
      "value": "30"
    },
    {
      "value": "30"
    }
  ]
}

class StachChart extends React.Component {
  render() {
    return (
      <ReactFusioncharts
        type="column2d"
        width="100%"
        height="60%"
        dataFormat="JSON"
        dataSource={dataSource}
      />
    );
  }
}

export default StachChart;
