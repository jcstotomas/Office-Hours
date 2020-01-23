import React from "react";
import axios from "axios";

export default class Registration extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      username: "",
      email: "",
      password: "",
      password_confirmation: "",
      reg_errors: ""
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
    const { username, email, password } = this.state;
    axios
      .post(
        "http://localhost:5000/api/users",
        {
          username: username,
          email: email,
          password: password
        }
        // { withCredentials: true }
      )
      .then(response => {
        if (response.status === 201) {
          console.log("created");
          localStorage.setItem("token", response.data.token);
          localStorage.setItem("username", username);
          this.props.handleSuccessfulAuth(response.data);
        }
      })
      .catch(error => {
        console.log("registration error", error);
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
            type="email"
            name="email"
            placeholder="Email"
            value={this.state.email}
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
          <input
            type="password"
            name="password_confirmation"
            placeholder="Password Confirmed"
            value={this.state.password_confirmation}
            onChange={this.handleChange}
            required
          />
          <button type="submit">Register</button>
        </form>
      </div>
    );
  }
}
