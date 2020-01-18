import React from "react";
import Registration from "./auth/Registration";

export default class Home extends React.Component {
  constructor(props) {
    super(props);
  }
  render() {
    return (
      <div>
        <h1>Home Page</h1>
        <h1>Status: {this.props.loggedIn}</h1>
        <Registration />
      </div>
    );
  }
}
