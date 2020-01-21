import React from "react";
import { BrowserRouter, Switch, Route } from "react-router-dom";
import Home from "./Home";
import Profile from "./Profile";

export default class App extends React.Component {
  constructor() {
    super();

    this.state = {
      loggedIn: "NOT_LOGGED_IN",
      user: {}
    };
    this.handleLogin = this.handleLogin.bind(this);
  }

  handleLogin(data) {
    this.setState({
      loggedIn: "LOGGED IN",
      user: data
    });
  }
  render() {
    return (
      <div className="app">
        <BrowserRouter>
          <Switch>
            <Route
              exact
              path={"/"}
              render={props => (
                <Home
                  {...props}
                  handleLogin={this.handleLogin}
                  loggedIn={this.state.loggedIn}
                />
              )}
            />
            <Route
              exact
              path={"/profile"}
              render={props => (
                <Profile {...props} loggedIn={this.state.loggedIn} />
              )}
            />
          </Switch>
        </BrowserRouter>
      </div>
    );
  }
}
