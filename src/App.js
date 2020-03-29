///
// src/index.jsx
///
import React from 'react'
import ReactDOM from 'react-dom'
import { BrowserRouter, Route } from '../node_modules/react-router-dom'

// Import Board and Scoreboard views
import { Board } from './components/Board'


// Create App component
class App extends React.Component {
  render() {
    return (
      <div className="app">
        <BrowserRouter>
          <Route path="/board" component={Board}/>
        </BrowserRouter>
      </div>
    )
  }
}

export default App;
