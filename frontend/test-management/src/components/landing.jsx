// src/LandingPage.jsx
import React from 'react';

function LandingPage() {
  const handleLogout = async () => {
    try {
      const response = await fetch('http://127.0.0.1:5000/auth/logout', {
        method: 'POST',
        credentials: 'include', // Send cookies with the request
      });

      const data = await response.json();

      if (response.status === 200) {
        // Clear the JWT cookie after successful logout
        document.cookie = "access_token=; expires=Thu, 01 Jan 1970 00:00:00 GMT; path=/";

        // Redirect to the login page
        window.location.href = '/login';
      } else {
        // Handle errors (invalid token, expired token, etc.)
        alert(data.error || 'Failed to log out. Please try again.');
      }
    } catch (err) {
      alert('An error occurred while logging out.');
    }
  };

  return (
    <div className="landing-page">
      <h1>Welcome to My App</h1>
      <p>Your go-to solution for amazing services.</p>
      <button onClick={() => (window.location.href = '/login')}>Get Started</button>
      <button onClick={handleLogout}>Logout</button> {/* Logout button */}
    </div>
  );
}

export default LandingPage;