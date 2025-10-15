const express = require('express');
const app = express();
const PORT = process.env.PORT || 3000;

app.get('/', (req, res) => {
  res.send('Hello from Node.js app — Deployed via GitHub Actions!');
});

app.listen(PORT, () => {
  console.log(`App listening on port ${PORT}`);
});
