import React, { useState } from "react";
import { TextField, Button, Card, CardContent, Typography, CircularProgress, Alert, Tabs, Tab, Box } from "@mui/material";

type Result = {
  label: string;
  score: number;
  message: string;
};

const NewsChecker: React.FC = () => {
  const [tab, setTab] = useState(0);
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState<Result | null>(null);
  const [error, setError] = useState<string | null>(null);

  const handleTabChange = (_: React.SyntheticEvent, newValue: number) => {
    setTab(newValue);
    setInput("");
    setResult(null);
    setError(null);
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    setResult(null);
    setError(null);

    try {
      const response = await fetch("http://localhost:8000/analyze", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text: input }),
      });
      if (!response.ok) {
        const data = await response.json();
        throw new Error(data.detail || "Unknown error");
      }
      const data = await response.json();
      setResult(data);
    } catch (err: any) {
      setError(err.message || "Something went wrong");
    } finally {
      setLoading(false);
    }
  };

  return (
    <Box sx={{ maxWidth: 600, mx: "auto", mt: 4 }}>
      <Tabs value={tab} onChange={handleTabChange} centered>
        <Tab label="Enter Text" />
        {/* <Tab label="Enter URL" />  // For future expansion */}
      </Tabs>
      <form onSubmit={handleSubmit}>
        <TextField
          label={tab === 0 ? "Paste article text here..." : "Paste article URL here..."}
          multiline={tab === 0}
          minRows={tab === 0 ? 4 : 1}
          fullWidth
          margin="normal"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          required
        />
        <Button type="submit" variant="contained" color="primary" disabled={loading || !input}>
          {loading ? <CircularProgress size={24} /> : "Check Authenticity"}
        </Button>
      </form>
      {error && <Alert severity="error" sx={{ mt: 2 }}>{error}</Alert>}
      {result && (
        <Card sx={{ mt: 4 }}>
          <CardContent>
            <Typography variant="h6" gutterBottom>
              Result: {result.label} ({result.score}%)
            </Typography>
            <Typography>{result.message}</Typography>
          </CardContent>
        </Card>
      )}
    </Box>
  );
};

export default NewsChecker;
