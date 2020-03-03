import React, { Component } from "react";
import {
  Row,
  Col,
  Table,
  Card,
  CardBody,
  CardHeader,
  UncontrolledCollapse,
  NavLink
} from "reactstrap";
import StackChart from "../../components/StackChart";
import DonutChart from "../../components/DonutChart";

const records = [
  {
    id: "Revenue",
    first: "",
    second: "",
    third: "",
    first1: "",
    second1: "",
    third1: ""
  },
  {
    id: "Saves",
    first: "",
    second: "",
    third: "",
    first1: "",
    second1: "",
    third1: ""
  }
];

const donutsData = [
  {
    dial: 50,
    title: "Saas, Rev, Sow, Pipeline",
    desc: "Decisions Resolved From Sow"
  },
  {
    dial: 40,
    title: "Key Accounts",
    desc: "Design Req"
  },
  {
    dial: 30,
    title: "Engineering",
    desc: "Design Req"
  },
  {
    dial: 70,
    title: "Forume Managers + Sows",
    desc: "Design Req"
  },
  {
    dial: 75,
    title: "Finances",
    desc: "Design Req"
  }
];

class Home extends Component {
  render() {
    return (
      <div className="container">
        <div className="home">
          <h1 className="ml-2 underline">Overview</h1>
          <Row>
            <Col className="flex">
              <h3 className="mr-2">Progress:</h3>
              <h3>This Month</h3>
            </Col>
            <Col>
              <h3 className="ml-5">Text To Date</h3>
            </Col>
          </Row>
          <Table bordered>
            <thead>
              <tr>
                <th className="td-id"></th>
                <th>5,000$</th>
                <th>vs Budget</th>
                <th>vs Pack Yr</th>
                <th className="td-gap"></th>
                <th>5,000$</th>
                <th>vs Budget</th>
                <th>vs Pack Yr</th>
              </tr>
            </thead>
            <tbody>
              {records.map((record, index) => {
                return (
                  <tr key={index}>
                    <th scope="row" className="td-id">
                      {record.id}
                    </th>
                    <td>{record.first}</td>
                    <td>{record.second}</td>
                    <td>{record.third}</td>
                    <td className="td-gap"></td>
                    <td>{record.first1}</td>
                    <td>{record.second1}</td>
                    <td>{record.third1}</td>
                  </tr>
                );
              })}
            </tbody>
          </Table>
          <Row>
            <Col>
              <h3 className="underline">Revenue, Sow + Pipeline vs Fy Tgt</h3>
              <div className="chart-box">
                <StackChart />
                <Card className="mt-5">
                  <CardHeader>
                    <h5 className="m-0">
                      <NavLink
                        className="custom-accordion-title d-block pt-2 pb-2"
                        id="group1"
                        href="#"
                      >
                        Key Success This Month
                        <span className="float-right">
                          <i className="mdi mdi-chevron-down accordion-arrow"></i>
                        </span>
                      </NavLink>
                    </h5>
                  </CardHeader>
                  <UncontrolledCollapse toggler="#group1">
                    <CardBody>There is no success this month :)</CardBody>
                  </UncontrolledCollapse>
                </Card>
              </div>
            </Col>
            <Col>
              <h3 className="underline">Business Health</h3>
              {donutsData.map(data => (
                <Row key={data.title}>
                  <Col lg="4">
                    <DonutChart dial={data.dial} />
                  </Col>
                  <Col lg="8">
                    <h4 className="underline pt-3">{data.title}</h4>
                    <h4 className="pink">{data.desc}</h4>
                  </Col>
                </Row>
              ))}
            </Col>
          </Row>
        </div>
      </div>
    );
  }
}

export default Home;
