var staticCacheName = 'djangopwa-v1'
self.addEventListener('install', (event) => {
    event.waitUntil(async function() {
      const cache = await caches.open(staticCacheName);
      await cache.addAll([
        '/'
        // etc
      ]);
    }());
  });

self.addEventListener('fetch', (event) => {
    event.respondWith(async function() {
      const cache = await caches.open(staticChacheName);
      const cachedResponse = await cache.match(event.request);
      if (cachedResponse) return cachedResponse;
      const networkResponse = await fetch(event.request);
      event.waitUntil(
        cache.put(event.request, networkResponse.clone())
      );
      return networkResponse;
    }());
  });