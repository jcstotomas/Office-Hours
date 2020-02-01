import React from "react";
import { BrowserRouter, Switch, Route } from "react-router-dom";
import Home from "./Home";
import Profile from "./Profile";
import Axios from "axios";

export default class App extends React.Component {
  constructor() {
    super();

    this.state = {
      loggedIn: "NOT_LOGGED_IN",
      user: {}
    };
    this.handleLogin = this.handleLogin.bind(this);
    this.check_login = this.check_login.bind(this);
    this.handle_logout = this.handle_logout.bind(this);
  }

  handle_logout() {
    this.setState({
      loggedIn: "NOT_LOGGED_IN",
      user: {}
    });
    localStorage.setItem("token", null);
    localStorage.setItem("username", null);
    localStorage.setItem("user", null);
  }

  check_login() {
    var token = localStorage.getItem("token");
    var username = localStorage.getItem("username");
    if (token != null) {
      Axios.get("http://localhost:5000/api/users/$".replace("$", username), {
        headers: { Authorization: `Bearer ` + token }
      })
        .then(response => {
          if (response.status === 200) {
            this.setState({
              loggedIn: "LOGGED_IN",
              user: response.data
            });
            console.log();
          }
          console.log(this.state);
        })
        .catch(error => {
          console.log("registration error", error);
        });
    } else {
      console.log("error");
    }
  }
  componentDidMount() {
    this.check_login();
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
                  handle_logout={this.handle_logout}
                  loggedIn={this.state.loggedIn}
                />
              )}
            />
            <Route
              exact
              path={"/profile"}
              render={props => (
                <Profile
                  {...props}
                  loggedIn={this.state.loggedIn}
                  handle_logout={this.handle_logout}
                  object={this.state.user}
                />
              )}
            />
          </Switch>
        </BrowserRouter>
      </div>
    );
  }
}
