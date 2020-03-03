import React, { Component } from "react";
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";
import Home from "./containers/home";
import PageNotFound from "./containers/errors/PageNotFound";

class App extends Component {
  render() {
    return (
      <Router>
        <div className="App">
          <Switch>
            <Route exact path="/" component={Home} />
            <Route path="/*" component={PageNotFound} />
          </Switch>
        </div>
      </Router>
    );
  }
}

export default App;
