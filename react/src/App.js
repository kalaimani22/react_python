import React, { useState } from "react";
import logo from "./logo.svg";
import "./App.css";

function App() {
  const [response, setResponse] = useState(null);
  fetch("https://react-python-1ckc.onrender.com/api/items/").then(
    (response) => {
      return response.json();
    }
  ).then((res)=>setResponse(res));
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        {response && response.map((item) => (
          <div key={item.id}>
            <h2>{item.name}</h2>
            <p>{item.description}</p>
          </div>
        ))}
      </header>
    </div>
  );
}


export default App;