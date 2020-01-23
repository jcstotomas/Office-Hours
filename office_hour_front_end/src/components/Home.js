import React from "react";
import Registration from "./auth/Registration";
import Login from "./auth/Login";

export default class Home extends React.Component {
  constructor(props) {
    super(props);

    this.handleSuccessfulAuth = this.handleSuccessfulAuth.bind(this);
    this.handleLogoutClick = this.handleLogoutClick.bind(this);
  }

  handleSuccessfulAuth(data) {
    this.props.handleLogin(data);
    this.props.history.push("/profile");
  }

  handleLogoutClick() {
    this.props.handle_logout();
    console.log("logged out");
  }

  render() {
    return (
      <div>
        <h1 className="home">Home Page</h1>
        <h1>Status: {this.props.loggedIn}</h1>
        <button onClick={() => this.handleLogoutClick()}>Logout</button>
        <Registration handleSuccessfulAuth={this.handleSuccessfulAuth} />
        <Login handleSuccessfulAuth={this.handleSuccessfulAuth} />
      </div>
    );
  }
}
