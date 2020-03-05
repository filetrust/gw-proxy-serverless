import React, { Component } from "react";
import { Row, Col, Table, Card, CardBody, CardHeader, UncontrolledCollapse, NavLink } from "reactstrap";
import StackChart from "../../components/StackChart";
import DonutChart from "../../components/DonutChart";

class Home extends Component {
  render() {
    return (
      <div className="container">
        <div className="home">
          <Row>
            <Col>
              <h3 className="mr-2">Future Markets + Sales</h3>

              <StackChart />

              <h3 className="mr-2">Product Services</h3>
              <Table bordered>
                <thead>
                  <tr>
                    <th>New/Devt</th>
                    <th>Investment</th>
                    <th>ROI</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td>x</td>
                    <td>y</td>
                    <td>z</td>
                  </tr>
                  <tr>
                    <td>x</td>
                    <td>y</td>
                    <td>z</td>
                  </tr>
                  <tr>
                    <td>x</td>
                    <td>y</td>
                    <td>z</td>
                  </tr>
                  <tr>
                    <td>x</td>
                    <td>y</td>
                    <td>z</td>
                  </tr>
                </tbody>
              </Table>
            </Col>
            <Col className="">
              <Row>
                <Col lg="7"></Col>
                <Col lg="5" style={{height: '150px'}}><DonutChart dial="70%" /></Col>
              </Row>
              <h3>Key Markets - Addressable + Trends</h3>
              <Table bordered>
                <thead>
                  <tr>
                    <th>Market</th>
                    <th>Relevant Products</th>
                    <th>Addressable Value</th>
                    <th>Competition + Why Glasswall</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td>x</td>
                    <td>y</td>
                    <td>z</td>
                    <td>a</td>
                  </tr>
                  <tr>
                    <td>x</td>
                    <td>y</td>
                    <td>z</td>
                    <td>a</td>
                  </tr>
                  <tr>
                    <td>x</td>
                    <td>y</td>
                    <td>z</td>
                    <td>a</td>
                  </tr>
                  <tr>
                    <td>x</td>
                    <td>y</td>
                    <td>z</td>
                    <td>a</td>
                  </tr>
                </tbody>
              </Table>
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
                      <UncontrolledCollapse toggler="#group1">
                    <CardBody>There is no success this month :)</CardBody>
                  </UncontrolledCollapse>

                      <h3>Marketing</h3>
                <Table bordered>
                <thead>
                  <tr>
                    <th>Initiative</th>
                    <th>Investment</th>
                    <th>ROI</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td>x</td>
                    <td>y</td>
                    <td>z</td>
                  </tr>
                  <tr>
                    <td>x</td>
                    <td>y</td>
                    <td>z</td>
                  </tr>
                  <tr>
                    <td>x</td>
                    <td>y</td>
                    <td>z</td>
                  </tr>
                  <tr>
                    <td>x</td>
                    <td>y</td>
                    <td>z</td>
                  </tr>
                </tbody>
              </Table>

            </Col>
          </Row>
          
          
        </div>
      </div>
    );
  }
}

export default Home;
