import React                      from 'react';
import {Icon, Table} from 'semantic-ui-react';
import './style.scss';

const data = [
  {metric: 'Average Deal Size', thisMonth: '', lastMonth: '', trend: 'side'},
  {metric: 'Average Days To Payment', thisMonth: '', lastMonth: '', trend: 'down'},
  {metric: 'Average WIP', thisMonth: '', lastMonth: '', trend: 'up'},
  {metric: 'Average Dest.', thisMonth: '', lastMonth: '', trend: 'up'},
];
const ProjectTable = () => (
  <React.Fragment>
    <Table celled>
      <Table.Header>
        <Table.Row>
          <Table.HeaderCell>
          </Table.HeaderCell>
          <Table.HeaderCell>
            This <br/> Month
          </Table.HeaderCell>
          <Table.HeaderCell>
            Last <br/> Month
          </Table.HeaderCell>
          <Table.HeaderCell>
            Trend
          </Table.HeaderCell>
        </Table.Row>
      </Table.Header>

      <Table.Body>
        {data.map(({metric, thisMonth, lastMonth, trend}) => {
          let iconName, iconColor = 'black';
          switch (trend) {
            case 'up':
              iconName = 'arrow up';
              iconColor = 'red';
              break;
            case 'side':
              iconName = 'arrows alternate horizontal';
              break;
            case 'down':
              iconName = 'arrow down';
              break;
            default:
          }
          return (
            <Table.Row key={metric}>
              <Table.Cell>{metric}</Table.Cell>
              <Table.Cell>{thisMonth}</Table.Cell>
              <Table.Cell>{lastMonth}</Table.Cell>
              <Table.Cell textAlign="center">
                <Icon name={iconName} color={iconColor} size="large"/>
              </Table.Cell>
            </Table.Row>
          );
        })}
      </Table.Body>
    </Table>
  </React.Fragment>
);

export default ProjectTable;
