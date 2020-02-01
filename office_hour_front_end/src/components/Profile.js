import React from "react";

export default class Profile extends React.Component {
  constructor(props) {
    super(props);
    console.log(props);
    this.handleLogoutClick = this.handleLogoutClick.bind(this);
  }

  handleLogoutClick() {
    this.props.handle_logout();
    console.log("logged out");
    this.props.history.push("/");
  }
  /*
about_me: "testing "
connection_count: 0
id: 5
interests: "Development"
major: "Computer Science"
name: "Jeremy Sto Tomas"
post_count: 0
skills_to_build: "building things"
username: "jeremystotomas"
year: "2019"
*/
  render() {
    return (
      <div>
        <h1>Profile Page</h1>
        <h1>{this.props.object["name"]}</h1>
        <h1>{this.props.object["major"]}</h1>
        <h2>Introduction: {this.props.object["about_me"]}</h2>
        <h2>Interests: {this.props.object["interests"]}</h2>
        <h2>Skills to Build: {this.props.object["skills_to_build"]}</h2>

        <h1>{localStorage.username}</h1>
        <button onClick={() => this.handleLogoutClick()}>Logout</button>
      </div>
    );
  }
}
