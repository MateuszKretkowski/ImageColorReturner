import React, { useEffect, useState } from "react";
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import { Items } from "./items";
import { Main } from "./Main";

function App() {


  return (
    <Router>

        <Routes>
          {/* Definiowanie tras */}
          <Route path="/" element={<Main />} />
          <Route path="/items" element={<Items />} />
        </Routes>
    </Router>
  );
}

export default App;


