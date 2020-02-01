import React from "react";
import axios from "axios";

export default class Login extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      username: "",
      password: "",
      login_errors: ""
    };

    this.handleSubmit = this.handleSubmit.bind(this);
    this.handleChange = this.handleChange.bind(this);
  }

  handleChange(event) {
    this.setState({
      [event.target.name]: event.target.value
    });
  }

  handleSubmit(event) {
    const { username, password } = this.state;
    axios
      .post(
        "http://localhost:5000/api/tokens",
        {},
        {
          auth: {
            username: username,
            password: password
          }
        }
      )
      .then(response => {
        console.log("res from login", response);
        if (response.status === 200) {
          localStorage.setItem("token", response.data.token);
          localStorage.setItem("username", username);
          localStorage.setItem("data", response.data.about);
          this.props.handleSuccessfulAuth(response.data);
        }
      })
      .catch(error => {
        console.log("login error", error);
      });
    event.preventDefault();
  }

  render() {
    return (
      <div>
        <form onSubmit={this.handleSubmit}>
          <input
            type="username"
            name="username"
            placeholder="username"
            value={this.state.username}
            onChange={this.handleChange}
            required
          />
          <input
            type="password"
            name="password"
            placeholder="Password"
            value={this.state.password}
            onChange={this.handleChange}
            required
          />

          <button type="submit">Login</button>
        </form>
      </div>
    );
  }
}
