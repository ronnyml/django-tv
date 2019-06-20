import '../scss/index.scss';

import React from 'react';
import ReactDOM from 'react-dom';

class App extends React.Component {
  render () {
    return (
      <h1 className="title">Django React TV</h1>
    )
  }
}
ReactDOM.render(<App />, document.getElementById('title'));