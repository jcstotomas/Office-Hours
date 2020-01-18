import React from "react";

export default class Profile extends React.Component {
  constructor(props) {
    super(props);
  }
  render() {
    return (
      <div>
        <h1>Profile Page</h1>
        <h1>{this.props.loggedIn}</h1>
      </div>
    );
  }
}
