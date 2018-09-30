import React, { Component } from 'react';
import logo from './cylinder.svg';
import './App.css';

class App extends Component {
  render() {
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <h1 className="App-title">Kill Your Friends</h1>
        </header>
        <p className="App-intro">
          To get started, insert your name:
        </p>
          <Link component={Lobby}><input type='text' placeholder='Name goes here'></input></Link>
        <p>
          <button>Next</button>
        </p>
      </div>
    )
  }
}

export default App;
