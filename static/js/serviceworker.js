var staticCacheName = 'djangopwa-v1';

self.addEventListener('install', (event) => {
  
  event.waitUntil(
    caches.open(staticCacheName).then((cache)  => {
      return cache.addAll([
        '/'
      ]);
    })
  );

});

self.addEventListener('fetch', (event) => {

  var requestUrl = new URL(event.request.url);

    if (requestUrl.origin === location.origin) {
      if ((requestUrl.pathname === '/')) {
        event.respondWith(caches.match('/'));
        return;
      }
    }

    event.respondWith(
      caches.match(event.request).then((response) => {
        return response || fetch(event.request);
      })
    );

});