const http = require('http');
const port = 3000;

const server = http.createServer((req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');
  res.end('Hello! Aplikasi ini dideploy otomatis lewat GitHub Actions & Docker!\n');
});

server.listen(port, () => {
  console.log(`Server running at port ${port}`);
});
