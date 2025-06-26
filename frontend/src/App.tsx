import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import NavBar from "./components/NavBar";
import Home from "./pages/Home";
import FAQ from "./pages/FAQ";
import About from "./pages/About";
import Feedback from "./pages/Feedback";
import { createTheme, ThemeProvider, CssBaseline } from "@mui/material";
import useMediaQuery from "@mui/material/useMediaQuery";

const App: React.FC = () => {
  // Detect system preference for dark mode
  const prefersDarkMode = useMediaQuery("(prefers-color-scheme: dark)");
  const [mode, setMode] = React.useState<"light" | "dark">(
    prefersDarkMode ? "dark" : "light"
  );

  const theme = React.useMemo(
    () =>
      createTheme({
        palette: {
          mode,
        },
      }),
    [mode]
  );

  const toggleTheme = () => {
    setMode((prev) => (prev === "light" ? "dark" : "light"));
  };

  return (
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <Router>
        <NavBar toggleTheme={toggleTheme} mode={mode} />
        {/* Add top margin to clear fixed NavBar (default AppBar height is 64px) */}
        <div style={{ marginTop: 72, padding: 24 }}>
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/faq" element={<FAQ />} />
            <Route path="/about" element={<About />} />
            <Route path="/feedback" element={<Feedback />} />
          </Routes>
        </div>
      </Router>
    </ThemeProvider>
  );
};

export default App;