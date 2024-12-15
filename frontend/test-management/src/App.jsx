import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Login from './components/login'; // Import Login component
import LandingPage from './components/landing';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Login />} /> {/* Default route for login */}
        <Route path="/landing" element={<LandingPage/>} /> {/* Replace with your actual dashboard component */}
      </Routes>
    </Router>
  );
}

export default App;
