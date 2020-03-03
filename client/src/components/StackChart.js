import React from "react";
import FusionCharts from "fusioncharts";
import charts from "fusioncharts/fusioncharts.charts";
import ReactFusioncharts from "react-fusioncharts";

// Resolves charts dependancy
charts(FusionCharts);

const dataSource = {
  chart: {
    showsum: "1",
    showBorder: "0",
    showToolTip: "0",
    plottooltext: "$label <b>$dataValue</b>",
    theme: "fusion",
    drawcrossline: "1",
    aligncaptiontocanvas: "0",
    showPlotBorder: "1",
    plotBorderThickness: "0.25",
    showxaxispercentvalues: "1",
    bgColor: "#ffffff",
    borderAlpha: "20",
    canvasBorderAlpha: "0",
    usePlotGradientColor: "0",
    plotBorderAlpha: "10",
    placevaluesInside: "1",
    valueFontColor: "#ffffff",
    showXAxisLine: "1",
    xAxisLineColor: "#999999",
    divlineColor: "#999999",
    divLineIsDashed: "1",
    showAlternateHGridColor: "0",
    subcaptionFontBold: "0",
    subcaptionFontSize: "14"
  },
  categories: [
    {
      category: [
        {
          label: ""
        }
      ]
    }
  ],
  trendlines: [
    {
      line: [
        {
          isTrendZone: "1",
          startvalue: "900",
          endValue: "905",
          tooltext: "TGT"
        }
      ]
    }
  ],
  dataset: [
    {
      seriesname: "Revenue",
      data: [
        {
          value: "150"
        }
      ]
    },
    {
      seriesname: "Stock",
      data: [
        {
          value: "350"
        }
      ]
    },
    {
      seriesname: "Pipeline",
      data: [
        {
          value: "300"
        }
      ]
    }
  ]
};

class StachChart extends React.Component {
  render() {
    return (
      <ReactFusioncharts
        type="stackedcolumn2d"
        width="70%"
        height="60%"
        dataFormat="JSON"
        dataSource={dataSource}
      />
    );
  }
}

export default StachChart;
