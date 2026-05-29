const http = require('http');
const fs = require('fs');
const path = require('path');

const root = process.cwd();
const port = Number(process.argv[2] || 8080);
const types = {
  '.html': 'text/html; charset=utf-8',
  '.css': 'text/css; charset=utf-8',
  '.js': 'text/javascript; charset=utf-8',
  '.png': 'image/png',
  '.jpg': 'image/jpeg',
  '.jpeg': 'image/jpeg',
  '.svg': 'image/svg+xml',
};

http.createServer((req, res) => {
  const requestPath = decodeURIComponent(req.url.split('?')[0]);
  const normalized = path.normalize(requestPath === '/' ? '/index.html' : requestPath);
  const file = path.join(root, normalized);

  if (!file.startsWith(root)) {
    res.writeHead(403);
    res.end('Forbidden');
    return;
  }

  fs.stat(file, (error, stat) => {
    if (error || !stat.isFile()) {
      res.writeHead(404);
      res.end('Not found');
      return;
    }

    res.writeHead(200, {
      'Content-Type': types[path.extname(file).toLowerCase()] || 'application/octet-stream',
      'Content-Length': stat.size,
      'Cache-Control': 'no-store',
    });
    fs.createReadStream(file).pipe(res);
  });
}).listen(port, '0.0.0.0');
