import React from "react";

export default class Profile extends React.Component {
  constructor(props) {
    super(props);

    this.handleLogoutClick = this.handleLogoutClick.bind(this);
  }

  handleLogoutClick() {
    this.props.handle_logout();
    console.log("logged out");
  }

  render() {
    return (
      <div>
        <h1>Profile Page</h1>
        <h1>{this.props.loggedIn}</h1>
        <h1>{localStorage.username}</h1>
        <button onClick={() => this.handleLogoutClick()}>Logout</button>
      </div>
    );
  }
}
