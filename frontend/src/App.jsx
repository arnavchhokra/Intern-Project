import React, { useState, useEffect } from "react";
import "./App.css";

function App() {
  const [threads, setThreads] = useState([]);

  useEffect(() => {
    async function fetchThreads() {
      const response = await fetch("http://127.0.0.1:8000/get_threads/");
      const data = await response.json();
      setThreads(data);
    }

    fetchThreads();
  }, []);

  return (
    <div className="App">
      <h1>Reddit Threads</h1>
      <div className="thread-list">
        {threads.map((thread, index) => (
          <div key={index} className="thread">
            <h2>{thread.title}</h2>
            <p>Author: {thread.author}</p>
            <a href={thread.url} target="_blank" rel="noopener noreferrer">
              View Thread
            </a>
          </div>
        ))}
      </div>
    </div>
  );
}

export default App;
