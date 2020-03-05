import React from "react";
import FusionCharts from "fusioncharts";
import FusionWidgets from "fusioncharts/fusioncharts.widgets";
import ReactFusioncharts from "react-fusioncharts";

// Resolves charts dependancy
FusionWidgets(FusionCharts);

class DonutChart extends React.Component {
  render() {
    const dataSource = {
      chart: {
        lowerlimit: "0",
        upperlimit: "100",
        showvalue: "1",
        numbersuffix: "%",
        theme: "fusion",
        showtooltip: "0",
        bgColor: "#ffffff",
        showBorder: "0",
        "showTickMarks": "0"
      },
      colorrange: {
        color: [
          {
            minvalue: "0",
            maxvalue: "33",
            code: "#F2726F"
          },
          {
            minvalue: "33",
            maxvalue: "66",
            code: "#FFC533"
          },
          {
            minvalue: "66",
            maxvalue: "99",
            code: "#62B58F"
          }
        ]
      },
      dials: {
        dial: [{value: this.props.dial}]
      }
    };
    return (
      <div className="donut-chart-box">
        <ReactFusioncharts
          type="angulargauge"
          width="100%"
          height="100%"
          dataFormat="JSON"
          dataSource={dataSource}
        />
      </div>
    );
  }
}

export default DonutChart;
