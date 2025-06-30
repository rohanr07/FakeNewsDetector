import React from "react";
import NewsChecker from "../components/NewsChecker";

const Home: React.FC = () => (
  <div>
    <h1>Fake News Detector</h1>
    <p>Check if your news is real or fake.</p>
    <NewsChecker />
  </div>
);

export default Home;