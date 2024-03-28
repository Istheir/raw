addEventListener('fetch', event => {
  event.respondWith(handleRequest(event.request));
});

async function handleRequest(request) {
  const url = new URL(request.url);

  // 检查请求的路径是否为特定路径，比如 /example
  if (url.pathname.startsWith("/Loyalsoldier/clash-rules/release")) {
    // 构建目标 URL
    const targetUrl = "https://raw.githubusercontent.com" + url.pathname;

    // 发起请求到目标 URL
    const response = await fetch(targetUrl, {
      headers: request.headers
    });
  if (url.pathname.startsWith("/Istheir/raw/master/Rules")) {
    // 构建目标 URL
    const targetUrl = "https://raw.githubusercontent.com" + url.pathname;

    // 发起请求到目标 URL
    const response = await fetch(targetUrl, {
      headers: request.headers
    });
    // 将目标服务器的响应返回给客户端
    return response;
  } else {
    // 如果不是特定路径，则直接请求原始网站
    return fetch(request);
  }
}
