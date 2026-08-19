import './App.css'
import { useState } from 'react'

function App() {
  const [player1, setPlayer1] = useState("Cole Palmer")
  const [player2, setPlayer2] = useState("Bruno Fernandes")
  return(
    <main>
      <h1>FPL Player Comparison|</h1>
      <div>
        <label>Player 1</label>
        <select
          value = {player1}
          onChange = {(event) => setPlayer1(event.target.value)}
        >
          <option value="Cole Palmer">Cole Palmer</option>
          <option value="Bruno Fernandes">Bruno Fernandes</option>
        </select>
      </div>

      <div>
        <label>Player 2</label>
        <select
          value = {player2}
          onChange = {(event) => setPlayer2(event.target.value)}
        >
          <option value="Cole Palmer">Cole Palmer</option>
          <option value="Bruno Fernandes">Bruno Fernandes</option>
        </select>
      </div>
      
      <div>
        <p>Player 1: {player1}</p>
        <p>Player 2: {player2}</p>
      </div>

    </main>
  )
  
}

export default App
