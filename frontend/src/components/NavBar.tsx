import React from "react";
import AppBar from "@mui/material/AppBar";
import Toolbar from "@mui/material/Toolbar";
import Typography from "@mui/material/Typography";
import Button from "@mui/material/Button";
import { Link as RouterLink } from "react-router-dom";
import Box from "@mui/material/Box";
import IconButton from "@mui/material/IconButton";
import Brightness4Icon from "@mui/icons-material/Brightness4";
import Brightness7Icon from "@mui/icons-material/Brightness7";
import { useTheme } from "@mui/material/styles";

interface NavBarProps {
  toggleTheme: () => void;
  mode: "light" | "dark";
}

const NavBar: React.FC<NavBarProps> = ({ toggleTheme, mode }) => {
  const theme = useTheme();

  return (
    <AppBar position="fixed" color="primary" sx={{ width: "100%" }}>
      <Toolbar>
        <Typography variant="h6" component="div" sx={{ flexGrow: 1 }}>
          Fake News Detector
        </Typography>
        <Box>
          <Button color="inherit" component={RouterLink} to="/">Home</Button>
          <Button color="inherit" component={RouterLink} to="/faq">FAQ</Button>
          <Button color="inherit" component={RouterLink} to="/about">About</Button>
          <Button color="inherit" component={RouterLink} to="/feedback">Feedback</Button>
        </Box>
        <IconButton sx={{ ml: 2 }} onClick={toggleTheme} color="inherit">
          {mode === "dark" ? <Brightness7Icon /> : <Brightness4Icon />}
        </IconButton>
      </Toolbar>
    </AppBar>
  );
};

export default NavBar;